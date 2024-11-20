# Django Model Filters Command Documentation

## Overview

The `model_filters` management command helps developers understand and navigate complex Django model relationships by displaying all possible field paths between models. 

For example, using models from the example project, running:
```bash
python manage.py model_filters sales.ShippingAddress
```

Would show all possible filtering paths starting from the ShippingAddress model in the sales app (178 in total):

| Field Path | Model | Field Name | Field Type | Models in Path |
|------------|-------|------------|------------|----------------|
| city | ShippingAddress | city | CharField | sales.ShippingAddress |
| country | ShippingAddress | country | CharField | sales.ShippingAddress |
| created_at | ShippingAddress | created_at | DateTimeField | sales.ShippingAddress |
| customer | ShippingAddress | customer | ForeignKey | sales.ShippingAddress |
| customer__company_name | Customer | company_name | CharField | sales.ShippingAddress,common.Customer |
| customer__created_at | Customer | created_at | DateTimeField | sales.ShippingAddress,common.Customer |
| customer__credit_limit | Customer | credit_limit | DecimalField | sales.ShippingAddress,common.Customer |
| customer__id | Customer | id | BigAutoField | sales.ShippingAddress,common.Customer |
| customer__is_active | Customer | is_active | BooleanField | sales.ShippingAddress,common.Customer |
| ... | | | | |

This tool is particularly useful when:

- Building complex database queries (e.g., finding all possible ways to join to a User model)
- Creating reports that span multiple related models
- Understanding the relationship structure of a large Django application
- Identifying available fields for filtering and annotations
- Helping generative AI to better understand the relationships in your project

## Command Syntax

```bash
python manage.py model_filters [options]
```

## Options

### Core Options

- **positional arg**: One or more app name(s), model name(s), or `app.Model` syntax to evaluate. Here we are evaluating all models in the `auth` app, the `sales.Order` model and the `Customer` model (e.g.: `common.Customer`).
  ```bash
  python manage.py model_filters auth sales.Order Customer
  ```

- **`--target-model`**: Filter paths leading to a specific model
  ```bash
  python manage.py model_filters sales --target-model User
  python manage.py model_filters sales --target-model auth.User
  ```

- **`--target-field`**: Filter paths leading to a specific model field
  ```bash
  python manage.py model_filters sales --target-field email
  ```

### Path Limiting Options

- **`--max-depth`**: Limit the number of relationship traversals (default: 4)
  ```bash
  python manage.py model_filters sales --max-depth 3
  ```

- **`--max-paths`**: Limit the maximum number of paths returned for *each* model of interest
  ```bash
  python manage.py model_filters sales --max-paths 10
  ```

### Additional Filters

- **`-e, --exclude`**: Exclude specific apps, models, or fields
  ```bash
  python manage.py model_filters sales -e auth Permission
  python manage.py model_filters sales -e customer__sales_creditcards customer__user
  ```

- **`--prefix`**: Include only models/fields in a path with a specific prefix
  ```bash
  python manage.py model_filters sales --prefix Customer
  ```

- **`--field-type`**: Filter by field type
  ```bash
  python manage.py model_filters sales --field-type DateTimeField
  ```

### Output Options

- **`--by-depth`**: Sort results by number of relationship traversals
- **`--by-model`**: Sort results by related model name
- **`-m, --markdown`**: Output in markdown format
- **`-o, --output`**: Export results to a file (supports .txt, .html, .htm, .md)

### Cache Control

- **`--use-cache`**: Use cached results if available (see also [settings](#settings))
- **`--clear-cache`**: Clear cached results before running

## Settings
All settings are optional, and should be added as dictionary key-value entries in the **`DJANGO_MODEL_INFO`** setting.

- **`CACHE_ENABLED`**: *bool* Enable caching of results (default: False)
- **`CACHE_ALWAYS`**: *bool* Always cache results, even if the --use-cache flag is not used (default: False)
- **`CACHE_ALIAS`**: *str* The cache alias to use for caching results (default: "default")
- **`CACHE_TIMEOUT`**: *int* The cache timeout in seconds (default: 3600)
- **`CACHE_KEY_PREFIX`**: *str* The prefix to use for cache keys (default: "model_filters:")

## Understanding Output

The command outputs a table with four columns:

1. **Field Path**: The full path to the field using Django's double-underscore notation
2. **Model**: The model containing the field
3. **Field Name**: The name of the field
4. **Field Type**: The Django field type
5. **Models in Path**: All of the models involved in the filter path

Example outputs for different filtering scenarios:

### Basic Model Fields
```bash
python manage.py model_filters auth.User --by-depth
```

| Field Path | Model | Field Name | Field Type | Models in Path |
|------------|-------|------------|------------|----------------|
| customer | User | customer | OneToOneRel | auth.User |
| date_joined | User | date_joined | DateTimeField | auth.User |
| email | User | email | EmailField | auth.User |
| first_name | User | first_name | CharField | auth.User |
| groups | User | groups | ManyToManyField | auth.User |
| id | User | id | AutoField | auth.User |
| ... | | | | |



### Filtering by Field Type
```bash
python manage.py model_filters sales.ShippingAddress --field-type DateTimeField
```

| Field Path | Model | Field Name | Field Type | Models in Path |
|------------|-------|------------|------------|----------------|
| created_at | ShippingAddress | created_at | DateTimeField | sales.ShippingAddress |
| customer__created_at | Customer | created_at | DateTimeField | sales.ShippingAddress,common.Customer |
| customer__orders__created_at | Order | created_at | DateTimeField | sales.ShippingAddress,common.Customer,sales.Order |
| customer__orders__items__created_at | OrderItem | created_at | DateTimeField | sales.ShippingAddress,common.Customer,sales.Order,sales.OrderItem |
| customer__orders__items__updated_at | OrderItem | updated_at | DateTimeField | sales.ShippingAddress,common.Customer,sales.Order,sales.OrderItem |
| customer__orders__order_date | Order | order_date | DateTimeField | sales.ShippingAddress,common.Customer,sales.Order |
| ... | | | | |


### Finding Related Models
```bash
python manage.py model_filters sales.ShippingAddress --target-model User
# or
python manage.py model_filters sales.ShippingAddress --target-model auth.User
```

| Field Path | Model | Field Name | Field Type | Models in Path |
|------------|-------|------------|------------|----------------|
| customer__user__customer | User | customer | OneToOneRel | sales.ShippingAddress,common.Customer,auth.User |
| customer__user__date_joined | User | date_joined | DateTimeField | sales.ShippingAddress,common.Customer,auth.User |
| customer__user__email | User | email | EmailField | sales.ShippingAddress,common.Customer,auth.User |
| customer__user__first_name | User | first_name | CharField | sales.ShippingAddress,common.Customer,auth.User |
| customer__user__groups | User | groups | ManyToManyField | sales.ShippingAddress,common.Customer,auth.User |
| customer__user__id | User | id | AutoField | sales.ShippingAddress,common.Customer,auth.User |
| ... | | | | |


```bash
python manage.py model_filters sales.ShippingAddress --target-field country
```
In this case there is only a single resulting path:

| Field Path | Model | Field Name | Field Type | Models in Path |
|------------|-------|------------|------------|----------------|
| country | ShippingAddress | country | CharField | sales.ShippingAddress |


## Advanced Features

### Combining Filters

You can combine multiple filters for precise results:

```bash
python manage.py model_filters \
    sales \
    --target-model User \
    --field-type EmailField \
    --max-depth 3 \
    --exclude auth
```

### Using Export Formats

Different export formats serve different purposes:
- `.md`: Documentation and GitHub
- `.html`: Web viewing
- `.txt`: Simple text processing


## Using model_filters: A Practical Guide

In this section, we'll explore how to use the model_filters command to help build efficient queries across related models in our application that handles customer orders, inventory, and analytics.

### Example Models Overview

Our example project manages inventory, sales, and analytics with several interconnected models. Here's a key subset of the relationships:

```python
# common/models.py
class Customer(BaseModel):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    company_name = models.CharField(max_length=200, blank=True)
    tax_id = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2, default=0)

# sales/models.py
class Order(BaseModel):
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

# inventory/models.py
class Product(BaseModel):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    suppliers = models.ManyToManyField(Supplier, through="ProductSupplier", related_name="products")
    weight = models.DecimalField(max_digits=8, decimal_places=2, help_text="Weight in kilograms", null=True, blank=True)
```

### Example Use Cases

#### 1. Find All Customer-Related Fields
When building a customer analytics dashboard, we need to understand all ways to access customer data. Let's use model_filters to discover these relationships:

```bash
python manage.py model_filters common.Customer
```

The output shows the rich customer data structure:

| Field Path | Model | Field Name | Field Type | Models in Path |
|------------|-------|------------|------------|----------------|
| company_name | Customer | company_name | CharField | common.Customer |
| created_at | Customer | created_at | DateTimeField | common.Customer |
| credit_limit | Customer | credit_limit | DecimalField | common.Customer |
| id | Customer | id | BigAutoField | common.Customer |
| is_active | Customer | is_active | BooleanField | common.Customer |
| notes | Customer | notes | TextField | common.Customer |
| orders | Customer | orders | ManyToOneRel | common.Customer |
| orders__created_at | Order | created_at | DateTimeField | common.Customer,sales.Order |
| orders__customer | Order | customer | ForeignKey | common.Customer,sales.Order |
| orders__id | Order | id | BigAutoField | common.Customer,sales.Order |
| orders__is_active | Order | is_active | BooleanField | common.Customer,sales.Order |
| orders__items | Order | items | ManyToOneRel | common.Customer,sales.Order |
| orders__items__created_at | OrderItem | created_at | DateTimeField | common.Customer,sales.Order,sales.OrderItem |
| orders__items__id | OrderItem | id | BigAutoField | common.Customer,sales.Order,sales.OrderItem |
| ... | | | | |

We can use these paths to create comprehensive customer analytics:
```python
# Find high-value customers with recent orders
from example_project.common.models import Customer
from django.db.models import Count, Max, Sum
from django.utils import timezone

thirty_days_ago = timezone.now() - timezone.timedelta(days=30)
Customer.objects.annotate(
    order_count=Count('orders'),
    total_spent=Sum('orders__total_amount'),
    last_order_date=Max('orders__order_date')
).filter(
    total_spent__gt=1000,
    last_order_date__gte=thirty_days_ago
).select_related('user')
```

#### 2. Product Supply Chain Analysis
For inventory management, we need to understand product relationships with suppliers and categories:

```bash
python manage.py model_filters inventory.Product --by-depth
```

The output reveals the product relationship hierarchy:

| Field Path | Model | Field Name | Field Type | Models in Path |
|------------|-------|------------|------------|----------------|
| category | Product | category | ForeignKey | inventory.Product |
| created_at | Product | created_at | DateTimeField | inventory.Product |
| description | Product | description | TextField | inventory.Product |
| id | Product | id | BigAutoField | inventory.Product |
| is_active | Product | is_active | BooleanField | inventory.Product |
| name | Product | name | CharField | inventory.Product |
| orderitem | Product | orderitem | ManyToOneRel | inventory.Product |
| performance_metrics | Product | performance_metrics | ManyToOneRel | inventory.Product |
| ... | | | | |
| productsupplier__cost | ProductSupplier | cost | DecimalField | inventory.Product,inventory.ProductSupplier |
| productsupplier__created_at | ProductSupplier | created_at | DateTimeField | inventory.Product,inventory.ProductSupplier |
| productsupplier__id | ProductSupplier | id | BigAutoField | inventory.Product,inventory.ProductSupplier |
| productsupplier__is_active | ProductSupplier | is_active | BooleanField | inventory.Product,inventory.ProductSupplier |
| productsupplier__is_preferred | ProductSupplier | is_preferred | BooleanField | inventory.Product,inventory.ProductSupplier |
| productsupplier__lead_time_days | ProductSupplier | lead_time_days | PositiveIntegerField | inventory.Product,inventory.ProductSupplier |
| ... | | | | |


Using these paths, we can analyze product supply chain metrics:
```python
# Find products with multiple suppliers and their cost variations
from example_project.inventory.models import Product
from django.db.models import Avg, Count, Min

Product.objects.annotate(
    supplier_count=Count('suppliers'),
    avg_cost=Avg('productsupplier__cost'),
    min_lead_time=Min('productsupplier__lead_time_days')
).filter(
    supplier_count__gt=1
).select_related('category')
```

#### 3. Sales Performance Analytics
To analyze sales performance, let's explore all available metrics fields:

```bash
python manage.py model_filters analytics.SalesMetrics
```

Output shows available metrics:

| Field Path | Model | Field Name | Field Type | Models in Path |
|------------|-------|------------|------------|----------------|
| average_order_value | SalesMetrics | average_order_value | DecimalField | analytics.SalesMetrics |
| conversion_rate | SalesMetrics | conversion_rate | DecimalField | analytics.SalesMetrics |
| created_at | SalesMetrics | created_at | DateTimeField | analytics.SalesMetrics |
| date | SalesMetrics | date | DateField | analytics.SalesMetrics |
| id | SalesMetrics | id | BigAutoField | analytics.SalesMetrics |
| is_active | SalesMetrics | is_active | BooleanField | analytics.SalesMetrics |
| notes | SalesMetrics | notes | TextField | analytics.SalesMetrics |
| total_orders | SalesMetrics | total_orders | IntegerField | analytics.SalesMetrics |
| ... | | | | |

This helps us build comprehensive sales analysis queries:
```python
# Analyze sales trends with rolling averages
from example_project.analytics.models import SalesMetrics
from django.db.models import Avg, F, RowRange, Window

SalesMetrics.objects.annotate(
    rolling_avg_orders=Window(
        expression=Avg('total_orders'),
        order_by=F('date').asc(),
        frame=RowRange(start=-6, end=0)
    ),
    rolling_conversion=Window(
        expression=Avg('conversion_rate'),
        order_by=F('date').asc(),
        frame=RowRange(start=-6, end=0)
    )
).order_by('-date')
```

## Complex Model Relationship Example

Let's build a complex query that analyzes product performance across our entire system, including sales, inventory, and customer data.

### Challenge
We want to create a comprehensive product analysis that includes:
- Sales performance metrics
- Inventory status
- Supplier relationships
- Customer purchasing patterns

### Using model_filters to Discover Paths

First, let's find all paths from Product to our analytics:

```bash
python manage.py model_filters inventory.Product --target-model ProductPerformance
```

This reveals the connections:

| Field Path | Model | Field Name | Field Type | Models in Path |
|------------|-------|------------|------------|----------------|
| performance_metrics__created_at | ProductPerformance | created_at | DateTimeField | inventory.Product,analytics.ProductPerformance |
| performance_metrics__date | ProductPerformance | date | DateField | inventory.Product,analytics.ProductPerformance |
| performance_metrics__id | ProductPerformance | id | BigAutoField | inventory.Product,analytics.ProductPerformance |
| performance_metrics__is_active | ProductPerformance | is_active | BooleanField | inventory.Product,analytics.ProductPerformance |
| performance_metrics__notes | ProductPerformance | notes | TextField | inventory.Product,analytics.ProductPerformance |
| performance_metrics__product | ProductPerformance | product | ForeignKey | inventory.Product,analytics.ProductPerformance |
| performance_metrics__profit_margin | ProductPerformance | profit_margin | DecimalField | inventory.Product,analytics.ProductPerformance |
| performance_metrics__revenue | ProductPerformance | revenue | DecimalField | inventory.Product,analytics.ProductPerformance |
| performance_metrics__units_sold | ProductPerformance | units_sold | PositiveIntegerField | inventory.Product,analytics.ProductPerformance |
| ... | | | | |

Now let's find order and customer related paths:
```bash
python manage.py model_filters inventory.Product --target-model Order OrderItem Customer
```

Output shows order connections:

| Field Path | Model | Field Name | Field Type | Models in Path |
|------------|-------|------------|------------|----------------|
| ... | | | | |
| orderitem__order | OrderItem | order | ForeignKey | inventory.Product,sales.OrderItem |
| orderitem__product | OrderItem | product | ForeignKey | inventory.Product,sales.OrderItem |
| orderitem__quantity | OrderItem | quantity | PositiveIntegerField | inventory.Product,sales.OrderItem |
| orderitem__unit_price | OrderItem | unit_price | DecimalField | inventory.Product,sales.OrderItem |
| ... | | | | |
| orderitem__updated_at | OrderItem | updated_at | DateTimeField | inventory.Product,sales.OrderItem |
| orderitem__order__created_at | Order | created_at | DateTimeField | inventory.Product,sales.OrderItem,sales.Order |
| orderitem__order__customer | Order | customer | ForeignKey | inventory.Product,sales.OrderItem,sales.Order |
| ... | | | | |
| orderitem__order__total_amount | Order | total_amount | DecimalField | inventory.Product,sales.OrderItem,sales.Order |
| orderitem__order__updated_at | Order | updated_at | DateTimeField | inventory.Product,sales.OrderItem,sales.Order |
| orderitem__order__customer__company_name | Customer | company_name | CharField | inventory.Product,sales.OrderItem,sales.Order,common.Customer |
| ... | | | | |


### Building the Analysis Query

Using the discovered paths, we can build a comprehensive analysis:

```python
from example_project.inventory.models import Product
from django.db.models import Avg, Count, Min, Sum, F, Q, Window
from django.db.models.functions import TruncMonth
from django.utils import timezone

# Comprehensive product analysis
current_year = timezone.now().year
Product.objects.annotate(
    # Sales metrics
    total_orders=Count('orderitem__order', distinct=True),
    total_revenue=Sum(F('orderitem__unit_price') * F('orderitem__quantity')),
    
    # Performance metrics
    avg_monthly_units=Avg(
        'performance_metrics__units_sold',
        filter=Q(performance_metrics__date__year=current_year)
    ),
    avg_profit_margin=Avg(
        'performance_metrics__profit_margin',
        filter=Q(performance_metrics__date__year=current_year)
    ),
    
    # Supplier metrics
    supplier_count=Count('suppliers', distinct=True),
    avg_lead_time=Avg('productsupplier__lead_time_days'),  # See previous section
    min_cost=Min('productsupplier__cost'),
    
    # Customer insights
    unique_customers=Count(
        'orderitem__order__customer',
        distinct=True
    ),
    corporate_orders=Count(
        'orderitem__order',
        filter=Q(orderitem__order__customer__company_name__isnull=False),
        distinct=True
    )
).select_related(
    'category'
).prefetch_related(
    'suppliers',
    'performance_metrics'
).order_by('-total_revenue')
```

This query provides a complete view of:
- Product sales performance
- Supplier diversity and cost efficiency
- Customer segment analysis
- Historical performance trends

## Performance Tips

1. **Use Caching**
   - Enable caching for repeated queries: `--use-cache`
   - Clear cache when needed: `--clear-cache`

2. **Limit Search Space**
   - Set appropriate `--max-depth`
   - Use `--max-paths` for large applications

3. **Filter Early**
   - Use `--target-model` and `--target-field` when possible
   - Apply `--exclude` for known irrelevant paths or models
   - Use `--prefix` to focus on specific model sets

## Best Practices

1. I smaller projects, start with broad queries and gradually add filters. In larger projects where there may be a huge number of paths, start with a narrow scope and broaden as needed
2. Use `--max-depth` to prevent deep recursion in complex relationships
3. Export results to markdown for documentation with `-m`
4. Use caching when running repeated queries during development
5. Clear cache when model relationships change

## Troubleshooting

### Common Issues

1. **Too Many Results**
   - Use `--max-paths` to limit output
   - Add specific filters
   - Increase `--max-depth` gradually

2. **Missing Paths**
   - Check `--max-depth` isn't too low
   - Verify excluded paths with `-e`
   - Ensure target model/field names are correct
