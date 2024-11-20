"""Analytics models for testing."""
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from example_project.common.models import BaseModel, Customer


class MetricsBase(BaseModel):
    """Abstract base class for all metric models."""

    date = models.DateField()
    value = models.DecimalField(max_digits=12, decimal_places=2)
    notes = models.TextField(blank=True)

    class Meta:
        """Meta options for the model."""

        abstract = True
        ordering = ["-date"]

    def __str__(self):
        return f"{self.__class__.__name__} - {self.date}"


class SalesMetrics(MetricsBase):
    """Daily sales metrics tracking."""

    total_orders = models.IntegerField()
    average_order_value = models.DecimalField(max_digits=10, decimal_places=2)
    conversion_rate = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])

    class Meta(MetricsBase.Meta):
        """Meta options for the model."""

        verbose_name_plural = "sales metrics"
        constraints = [models.CheckConstraint(check=Q(conversion_rate__lte=100), name="conversion_rate_percentage")]


class ProductPerformance(MetricsBase):
    """Product performance metrics."""

    product = models.ForeignKey("inventory.Product", on_delete=models.CASCADE, related_name="performance_metrics")
    units_sold = models.PositiveIntegerField()
    revenue = models.DecimalField(max_digits=12, decimal_places=2)
    profit_margin = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta(MetricsBase.Meta):
        """Meta options for the model."""

        unique_together = ["date", "product"]


class CustomerSegment(Customer):
    """Customer segmentation proxy model.

    Extends Customer model with additional analysis methods.
    """

    class Meta:
        """Meta options for the model."""

        proxy = True

    def get_lifetime_value(self):
        """Calculate customer lifetime value.

        Returns:
            Decimal: Customer lifetime value based on total spent and account age
        """
        months_active = (timezone.now() - self.created_at).days / 30.44  # Average days per month

        if months_active == 0:
            return Decimal("0.00")

        return Decimal(str(self.total_spent / months_active))


class DailyRevenue(models.Model):
    """Unmanaged model for daily revenue view.

    Maps to a database view rather than a table.
    """

    date = models.DateField(primary_key=True)
    revenue = models.DecimalField(max_digits=12, decimal_places=2)
    order_count = models.IntegerField()

    class Meta:
        """Meta options for the model."""

        managed = False
        db_table = "daily_revenue_view"
