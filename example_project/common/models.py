"""Common models for Testing."""
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """Abstract base model providing common fields and functionality.

    Attributes:
        created_at: Timestamp of when the record was created
        updated_at: Timestamp of when the record was last updated
        is_active: Boolean indicating if the record is active
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        """Meta options for the BaseModel."""

        abstract = True

    def activate(self):
        """Activate the record"""
        self.is_active = True
        self.save()

    def deactivate(self):
        """Deactivate the record"""
        self.is_active = False
        self.save()


class Customer(BaseModel):
    """Customer model with basic and extended profile information."""

    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    company_name = models.CharField(max_length=200, blank=True)
    tax_id = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        """Meta options for the model."""

        indexes = [models.Index(fields=["user", "company_name"])]

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.company_name})"

    @property
    def total_spent(self):
        """Calculate total amount spent by customer."""
        return self.orders.aggregate(total=models.Sum("total_amount"))["total"] or 0
