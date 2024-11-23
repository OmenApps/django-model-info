
## sales.CreditCard

| Field Path | Model | Field Name | Field Type | Models in Path |
|------------|-------|------------|------------|----------------|
| customer__company_name | Customer | company_name | CharField | sales.CreditCard,common.Customer |
| customer__phone | Customer | phone | CharField | sales.CreditCard,common.Customer |
| customer__tax_id | Customer | tax_id | CharField | sales.CreditCard,common.Customer |
| customer__orders__shipping_address__city | ShippingAddress | city | CharField | sales.CreditCard,common.Customer,sales.Order,sales.ShippingAddress |
| customer__orders__shipping_address__country | ShippingAddress | country | CharField | sales.CreditCard,common.Customer,sales.Order,sales.ShippingAddress |
| customer__orders__shipping_address__name | ShippingAddress | name | CharField | sales.CreditCard,common.Customer,sales.Order,sales.ShippingAddress |
| customer__orders__shipping_address__phone | ShippingAddress | phone | CharField | sales.CreditCard,common.Customer,sales.Order,sales.ShippingAddress |
| customer__orders__shipping_address__postal_code | ShippingAddress | postal_code | CharField | sales.CreditCard,common.Customer,sales.Order,sales.ShippingAddress |
| customer__orders__shipping_address__state | ShippingAddress | state | CharField | sales.CreditCard,common.Customer,sales.Order,sales.ShippingAddress |
| customer__orders__shipping_address__street_address1 | ShippingAddress | street_address1 | CharField | sales.CreditCard,common.Customer,sales.Order,sales.ShippingAddress |
| customer__orders__shipping_address__street_address2 | ShippingAddress | street_address2 | CharField | sales.CreditCard,common.Customer,sales.Order,sales.ShippingAddress |
| customer__shipping_addresses__city | ShippingAddress | city | CharField | sales.CreditCard,common.Customer,sales.ShippingAddress |
| customer__shipping_addresses__country | ShippingAddress | country | CharField | sales.CreditCard,common.Customer,sales.ShippingAddress |
| customer__shipping_addresses__name | ShippingAddress | name | CharField | sales.CreditCard,common.Customer,sales.ShippingAddress |
| customer__shipping_addresses__phone | ShippingAddress | phone | CharField | sales.CreditCard,common.Customer,sales.ShippingAddress |
| customer__shipping_addresses__postal_code | ShippingAddress | postal_code | CharField | sales.CreditCard,common.Customer,sales.ShippingAddress |
| customer__shipping_addresses__state | ShippingAddress | state | CharField | sales.CreditCard,common.Customer,sales.ShippingAddress |
| customer__shipping_addresses__street_address1 | ShippingAddress | street_address1 | CharField | sales.CreditCard,common.Customer,sales.ShippingAddress |
| customer__shipping_addresses__street_address2 | ShippingAddress | street_address2 | CharField | sales.CreditCard,common.Customer,sales.ShippingAddress |

## sales.ShippingAddress

| Field Path | Model | Field Name | Field Type | Models in Path |
|------------|-------|------------|------------|----------------|
| customer__company_name | Customer | company_name | CharField | sales.ShippingAddress,common.Customer |
| customer__phone | Customer | phone | CharField | sales.ShippingAddress,common.Customer |
| customer__tax_id | Customer | tax_id | CharField | sales.ShippingAddress,common.Customer |
| order__customer__company_name | Customer | company_name | CharField | sales.ShippingAddress,sales.Order,common.Customer |
| order__customer__phone | Customer | phone | CharField | sales.ShippingAddress,sales.Order,common.Customer |
| order__customer__tax_id | Customer | tax_id | CharField | sales.ShippingAddress,sales.Order,common.Customer |
| city | ShippingAddress | city | CharField | sales.ShippingAddress |
| country | ShippingAddress | country | CharField | sales.ShippingAddress |
| name | ShippingAddress | name | CharField | sales.ShippingAddress |
| phone | ShippingAddress | phone | CharField | sales.ShippingAddress |
| postal_code | ShippingAddress | postal_code | CharField | sales.ShippingAddress |
| state | ShippingAddress | state | CharField | sales.ShippingAddress |
| street_address1 | ShippingAddress | street_address1 | CharField | sales.ShippingAddress |
| street_address2 | ShippingAddress | street_address2 | CharField | sales.ShippingAddress |

## sales.OrderItem

| Field Path | Model | Field Name | Field Type | Models in Path |
|------------|-------|------------|------------|----------------|
| order__customer__company_name | Customer | company_name | CharField | sales.OrderItem,sales.Order,common.Customer |
| order__customer__phone | Customer | phone | CharField | sales.OrderItem,sales.Order,common.Customer |
| order__customer__tax_id | Customer | tax_id | CharField | sales.OrderItem,sales.Order,common.Customer |
| order__shipping_address__customer__company_name | Customer | company_name | CharField | sales.OrderItem,sales.Order,sales.ShippingAddress,common.Customer |
| order__shipping_address__customer__phone | Customer | phone | CharField | sales.OrderItem,sales.Order,sales.ShippingAddress,common.Customer |
| order__shipping_address__customer__tax_id | Customer | tax_id | CharField | sales.OrderItem,sales.Order,sales.ShippingAddress,common.Customer |
| order__customer__shipping_addresses__city | ShippingAddress | city | CharField | sales.OrderItem,sales.Order,common.Customer,sales.ShippingAddress |
| order__customer__shipping_addresses__country | ShippingAddress | country | CharField | sales.OrderItem,sales.Order,common.Customer,sales.ShippingAddress |
| order__customer__shipping_addresses__name | ShippingAddress | name | CharField | sales.OrderItem,sales.Order,common.Customer,sales.ShippingAddress |
| order__customer__shipping_addresses__phone | ShippingAddress | phone | CharField | sales.OrderItem,sales.Order,common.Customer,sales.ShippingAddress |
| order__customer__shipping_addresses__postal_code | ShippingAddress | postal_code | CharField | sales.OrderItem,sales.Order,common.Customer,sales.ShippingAddress |
| order__customer__shipping_addresses__state | ShippingAddress | state | CharField | sales.OrderItem,sales.Order,common.Customer,sales.ShippingAddress |
| order__customer__shipping_addresses__street_address1 | ShippingAddress | street_address1 | CharField | sales.OrderItem,sales.Order,common.Customer,sales.ShippingAddress |
| order__customer__shipping_addresses__street_address2 | ShippingAddress | street_address2 | CharField | sales.OrderItem,sales.Order,common.Customer,sales.ShippingAddress |
| order__shipping_address__city | ShippingAddress | city | CharField | sales.OrderItem,sales.Order,sales.ShippingAddress |
| order__shipping_address__country | ShippingAddress | country | CharField | sales.OrderItem,sales.Order,sales.ShippingAddress |
| order__shipping_address__name | ShippingAddress | name | CharField | sales.OrderItem,sales.Order,sales.ShippingAddress |
| order__shipping_address__phone | ShippingAddress | phone | CharField | sales.OrderItem,sales.Order,sales.ShippingAddress |
| order__shipping_address__postal_code | ShippingAddress | postal_code | CharField | sales.OrderItem,sales.Order,sales.ShippingAddress |
| order__shipping_address__state | ShippingAddress | state | CharField | sales.OrderItem,sales.Order,sales.ShippingAddress |
| order__shipping_address__street_address1 | ShippingAddress | street_address1 | CharField | sales.OrderItem,sales.Order,sales.ShippingAddress |
| order__shipping_address__street_address2 | ShippingAddress | street_address2 | CharField | sales.OrderItem,sales.Order,sales.ShippingAddress |

## sales.Order

| Field Path | Model | Field Name | Field Type | Models in Path |
|------------|-------|------------|------------|----------------|
| customer__company_name | Customer | company_name | CharField | sales.Order,common.Customer |
| customer__phone | Customer | phone | CharField | sales.Order,common.Customer |
| customer__tax_id | Customer | tax_id | CharField | sales.Order,common.Customer |
| shipping_address__customer__company_name | Customer | company_name | CharField | sales.Order,sales.ShippingAddress,common.Customer |
| shipping_address__customer__phone | Customer | phone | CharField | sales.Order,sales.ShippingAddress,common.Customer |
| shipping_address__customer__tax_id | Customer | tax_id | CharField | sales.Order,sales.ShippingAddress,common.Customer |
| customer__shipping_addresses__city | ShippingAddress | city | CharField | sales.Order,common.Customer,sales.ShippingAddress |
| customer__shipping_addresses__country | ShippingAddress | country | CharField | sales.Order,common.Customer,sales.ShippingAddress |
| customer__shipping_addresses__name | ShippingAddress | name | CharField | sales.Order,common.Customer,sales.ShippingAddress |
| customer__shipping_addresses__phone | ShippingAddress | phone | CharField | sales.Order,common.Customer,sales.ShippingAddress |
| customer__shipping_addresses__postal_code | ShippingAddress | postal_code | CharField | sales.Order,common.Customer,sales.ShippingAddress |
| customer__shipping_addresses__state | ShippingAddress | state | CharField | sales.Order,common.Customer,sales.ShippingAddress |
| customer__shipping_addresses__street_address1 | ShippingAddress | street_address1 | CharField | sales.Order,common.Customer,sales.ShippingAddress |
| customer__shipping_addresses__street_address2 | ShippingAddress | street_address2 | CharField | sales.Order,common.Customer,sales.ShippingAddress |
| shipping_address__city | ShippingAddress | city | CharField | sales.Order,sales.ShippingAddress |
| shipping_address__country | ShippingAddress | country | CharField | sales.Order,sales.ShippingAddress |
| shipping_address__name | ShippingAddress | name | CharField | sales.Order,sales.ShippingAddress |
| shipping_address__phone | ShippingAddress | phone | CharField | sales.Order,sales.ShippingAddress |
| shipping_address__postal_code | ShippingAddress | postal_code | CharField | sales.Order,sales.ShippingAddress |
| shipping_address__state | ShippingAddress | state | CharField | sales.Order,sales.ShippingAddress |
| shipping_address__street_address1 | ShippingAddress | street_address1 | CharField | sales.Order,sales.ShippingAddress |
| shipping_address__street_address2 | ShippingAddress | street_address2 | CharField | sales.Order,sales.ShippingAddress |

## sales.BankAccount

| Field Path | Model | Field Name | Field Type | Models in Path |
|------------|-------|------------|------------|----------------|
| customer__company_name | Customer | company_name | CharField | sales.BankAccount,common.Customer |
| customer__phone | Customer | phone | CharField | sales.BankAccount,common.Customer |
| customer__tax_id | Customer | tax_id | CharField | sales.BankAccount,common.Customer |
| customer__orders__shipping_address__city | ShippingAddress | city | CharField | sales.BankAccount,common.Customer,sales.Order,sales.ShippingAddress |
| customer__orders__shipping_address__country | ShippingAddress | country | CharField | sales.BankAccount,common.Customer,sales.Order,sales.ShippingAddress |
| customer__orders__shipping_address__name | ShippingAddress | name | CharField | sales.BankAccount,common.Customer,sales.Order,sales.ShippingAddress |
| customer__orders__shipping_address__phone | ShippingAddress | phone | CharField | sales.BankAccount,common.Customer,sales.Order,sales.ShippingAddress |
| customer__orders__shipping_address__postal_code | ShippingAddress | postal_code | CharField | sales.BankAccount,common.Customer,sales.Order,sales.ShippingAddress |
| customer__orders__shipping_address__state | ShippingAddress | state | CharField | sales.BankAccount,common.Customer,sales.Order,sales.ShippingAddress |
| customer__orders__shipping_address__street_address1 | ShippingAddress | street_address1 | CharField | sales.BankAccount,common.Customer,sales.Order,sales.ShippingAddress |
| customer__orders__shipping_address__street_address2 | ShippingAddress | street_address2 | CharField | sales.BankAccount,common.Customer,sales.Order,sales.ShippingAddress |
| customer__shipping_addresses__city | ShippingAddress | city | CharField | sales.BankAccount,common.Customer,sales.ShippingAddress |
| customer__shipping_addresses__country | ShippingAddress | country | CharField | sales.BankAccount,common.Customer,sales.ShippingAddress |
| customer__shipping_addresses__name | ShippingAddress | name | CharField | sales.BankAccount,common.Customer,sales.ShippingAddress |
| customer__shipping_addresses__phone | ShippingAddress | phone | CharField | sales.BankAccount,common.Customer,sales.ShippingAddress |
| customer__shipping_addresses__postal_code | ShippingAddress | postal_code | CharField | sales.BankAccount,common.Customer,sales.ShippingAddress |
| customer__shipping_addresses__state | ShippingAddress | state | CharField | sales.BankAccount,common.Customer,sales.ShippingAddress |
| customer__shipping_addresses__street_address1 | ShippingAddress | street_address1 | CharField | sales.BankAccount,common.Customer,sales.ShippingAddress |
| customer__shipping_addresses__street_address2 | ShippingAddress | street_address2 | CharField | sales.BankAccount,common.Customer,sales.ShippingAddress |
