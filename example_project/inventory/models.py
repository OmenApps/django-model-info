"""Inventory models for testing."""
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import F, Q
from django.utils.translation import gettext_lazy as _

from example_project.common.models import BaseModel


class Category(BaseModel):
    """Product category model with hierarchical structure using MPTT."""

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    description = models.TextField(blank=True)

    class Meta:
        """Meta options for the model."""

        verbose_name_plural = "categories"
        indexes = [models.Index(fields=["name", "slug"]), models.Index(fields=["parent", "name"])]
        constraints = [models.CheckConstraint(check=~Q(parent=F("id")), name="prevent_self_parent")]

    def __str__(self):
        return self.name

    @property
    def full_path(self):
        """Return the full category path from root to this node."""
        if self.parent:
            return f"{self.parent.full_path} > {self.name}"
        return self.name


class Supplier(BaseModel):
    """Supplier model representing product vendors."""

    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50, unique=True)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    address = models.TextField()
    payment_terms = models.IntegerField(help_text="Payment terms in days", validators=[MinValueValidator(0)])
    tax_id = models.CharField(max_length=50, blank=True)

    class Meta:
        """Meta options for the model."""

        ordering = ["name"]
        indexes = [models.Index(fields=["code", "name"])]

    def __str__(self):
        return f"{self.code} - {self.name}"


class ProductQuerySet(models.QuerySet):
    """Custom queryset methods for the Product model."""

    def active(self):
        """Return only active products."""
        return self.filter(is_active=True)

    def low_stock(self, threshold=10):
        """Return products with stock below threshold."""
        return self.filter(inventoryitem__quantity__lt=threshold)

    def out_of_stock(self):
        """Return products with zero stock."""
        return self.filter(inventoryitem__quantity=0)


class ProductManager(models.Manager.from_queryset(ProductQuerySet)):
    """Custom manager for the Product model."""

    def get_queryset(self):
        """Return the base queryset with related category."""
        return super().get_queryset().select_related("category")


class Product(BaseModel):
    """Product model representing items available for sale.

    Example:
        ```python
        product = Product.objects.create(
            name="Widget",
            sku="WDG-001",
            price=Decimal('19.99')
        )
        ```
    """

    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    suppliers = models.ManyToManyField(Supplier, through="ProductSupplier", related_name="products")
    weight = models.DecimalField(max_digits=8, decimal_places=2, help_text="Weight in kilograms", null=True, blank=True)

    objects = ProductManager()

    class Meta:
        """Meta options for the model."""

        indexes = [models.Index(fields=["sku", "name"]), models.Index(fields=["category", "-created_at"])]
        constraints = [models.CheckConstraint(check=Q(price__gt=0), name="price_positive")]

    def __str__(self):
        return f"{self.sku} - {self.name}"

    def clean(self):
        if self.weight and self.weight < 0:
            raise ValidationError({"weight": "Weight cannot be negative"})


class ProductSupplier(BaseModel):
    """Intermediate model for Product-Supplier relationship."""

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    supplier_sku = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    lead_time_days = models.PositiveIntegerField()
    is_preferred = models.BooleanField(default=False)

    class Meta:
        """Meta options for the model."""

        unique_together = ["product", "supplier"]
        indexes = [models.Index(fields=["product", "supplier", "is_preferred"])]
