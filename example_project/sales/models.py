"""Sales models for testing."""
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from example_project.common.models import BaseModel, Customer


class PaymentMethod(BaseModel):
    """Abstract base class for payment methods."""

    name = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)
    customer = models.ForeignKey(
        "common.Customer",
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

    class Meta:
        """Meta options for the model."""

        abstract = True


class CreditCard(PaymentMethod):
    """Credit card payment method."""

    last_4_digits = models.CharField(max_length=4)
    expiry_month = models.PositiveIntegerField()
    expiry_year = models.PositiveIntegerField()
    card_type = models.CharField(max_length=20)

    class Meta:
        """Meta options for the model."""

        constraints = [
            models.CheckConstraint(check=Q(expiry_month__gte=1) & Q(expiry_month__lte=12), name="valid_expiry_month")
        ]


class BankAccount(PaymentMethod):
    """Bank account payment method."""

    account_number = models.CharField(max_length=50)
    routing_number = models.CharField(max_length=20)
    account_type = models.CharField(max_length=20)


class ShippingAddress(BaseModel):
    """Shipping address model for customer orders.

    Tracks both customer's saved addresses and one-off order addresses.
    """

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="shipping_addresses")
    name = models.CharField(max_length=200)
    street_address1 = models.CharField(max_length=200)
    street_address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)
    phone = models.CharField(max_length=20)
    delivery_instructions = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "shipping addresses"
        indexes = [models.Index(fields=["customer", "is_default"]), models.Index(fields=["postal_code", "city"])]
        constraints = [
            models.CheckConstraint(
                check=Q(street_address1__isnull=False) & ~Q(street_address1=""), name="required_street_address"
            )
        ]

    def __str__(self):
        return f"{self.name} - {self.street_address1}, {self.city}"

    def save(self, *args, **kwargs):
        """Override save to ensure only one default address per customer."""
        if self.is_default:
            self.__class__.objects.filter(customer=self.customer, is_default=True).exclude(id=self.id).update(
                is_default=False
            )
        super().save(*args, **kwargs)

    def _get_address_parts(self):
        """Return address parts as a list."""
        return [
            self.street_address1,
            self.street_address2,
            self.city,
            self.state,
            self.postal_code,
            self.country,
        ]

    @property
    def full_address(self):
        """Return complete formatted address."""
        address_parts = self._get_address_parts()
        return ", ".join(filter(None, address_parts))


class OrderQuerySet(models.QuerySet):
    """Custom queryset methods for the Order model."""

    def pending(self):
        """Return pending orders."""
        return self.filter(status="pending")

    def completed(self):
        """Return completed orders."""
        return self.filter(status="completed")

    def cancelled(self):
        """Return cancelled orders."""
        return self.filter(status="cancelled")


class OrderManager(models.Manager.from_queryset(OrderQuerySet)):
    """Custom manager for the Order model."""

    def get_queryset(self):
        """Select related customer for all queries."""
        return super().get_queryset().select_related("customer")


class Order(BaseModel):
    """Order model representing customer purchases.

    Args:
        customer: The customer who placed the order
        status: Current order status

    Raises:
        ValidationError: If order total is negative
    """

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="orders")
    order_number = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    order_date = models.DateTimeField(auto_now_add=True)
    shipping_address = models.ForeignKey("ShippingAddress", on_delete=models.PROTECT)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True)

    objects = OrderManager()

    class Meta:
        """Meta options for the model."""

        ordering = ["-order_date"]
        indexes = [models.Index(fields=["order_number", "status"]), models.Index(fields=["customer", "-order_date"])]

    def __str__(self):
        return f"Order {self.order_number}"

    def clean(self):
        """Validate order total amount."""
        if self.total_amount < 0:
            raise ValidationError("Total amount cannot be negative")


class OrderItem(BaseModel):
    """Individual item within an order."""

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("inventory.Product", on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ["order", "product"]

    @property
    def subtotal(self):
        """Calculate subtotal for this item."""
        return self.quantity * self.unit_price
