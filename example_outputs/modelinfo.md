# sales.CreditCard

## Model Info

| Key | Value |
|---|-----|
| Model Name | CreditCard |
| Verbose Name | credit card |
| Verbose Name Plural | credit cards |
| Docstring | <p>Credit card payment method.</p> |
| Is Abstract | False |
| Is Proxy | False |
| Is Managed | True |
| Ordering | [] |
| Permissions | [] |
| Default Permissions | ('add', 'change', 'delete', 'view') |
| Indexes | [] |
| Constraints | [<CheckConstraint: condition=(AND: ('expiry_month__gte', 1), ('expiry_month__lte', 12)) name='valid_expiry_month'>] |
| Database Table | sales_creditcard |
| Base Manager | None |
| Default Manager | None |
| File | /home/watervize/omenapps_packages/django-model-info/example_project/sales/models.py |
| Starting Line Number | 28 |
| Method Resolution Order | (<class 'example_project.sales.models.CreditCard'>, <class 'example_project.sales.models.PaymentMethod'>, <class 'example_project.common.models.BaseModel'>, <class 'django.db.models.base.Model'>, <class 'django.db.models.utils.AltersData'>, <class 'object'>) |

## Fields

| Field Name | Field Type | Database Column | Database Type | Verbose Name |
|----------|----------|---------------|-------------|------------|
| `card_type` | CharField | card_type | varchar(20) | card type |
| `created_at` | DateTimeField | created_at | datetime | created at |
| `customer` | ForeignKey | customer_id | bigint | customer |
| `expiry_month` | PositiveIntegerField | expiry_month | integer unsigned | expiry month |
| `expiry_year` | PositiveIntegerField | expiry_year | integer unsigned | expiry year |
| `id (pk)` | BigAutoField | id | integer | ID |
| `is_active` | BooleanField | is_active | bool | is active |
| `is_default` | BooleanField | is_default | bool | is default |
| `last_4_digits` | CharField | last_4_digits | varchar(4) | last 4 digits |
| `name` | CharField | name | varchar(100) | name |
| `updated_at` | DateTimeField | updated_at | datetime | updated at |

## Relations

| Field Name | Field Type | Database Column | Database Type | Related Model | Related Name |
|----------|----------|---------------|-------------|-------------|------------|
| `customer` | ForeignKey | customer_id | bigint | common.Customer | sales_creditcard_related |

## Methods

### Other Methods

| Method Name | Signature | Docstring | File | Line Number |
|-----------|---------|---------|----|-----------|
| `activate` | `(self)` | <p>Activate the record</p> | watervize/omenapps_packages/django-model-info/example_project/common/models.py | 24 |
| `deactivate` | `(self)` | <p>Deactivate the record</p> | watervize/omenapps_packages/django-model-info/example_project/common/models.py | 29 |
| `get_next_by_created_at` | `(self, *, field=<django.db.models.fields.DateTimeField: created_at>, is_next=True, **kwargs)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |
| `get_next_by_updated_at` | `(self, *, field=<django.db.models.fields.DateTimeField: updated_at>, is_next=True, **kwargs)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |
| `get_previous_by_created_at` | `(self, *, field=<django.db.models.fields.DateTimeField: created_at>, is_next=False, **kwargs)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |
| `get_previous_by_updated_at` | `(self, *, field=<django.db.models.fields.DateTimeField: updated_at>, is_next=False, **kwargs)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |


### Dunder Methods

| Method Name | Signature | Docstring | File | Line Number |
|-----------|---------|---------|----|-----------|
| `__class__` | `(name, bases, attrs, **kwargs)` | <p>Metaclass for all models.</p> | python3.13/site-packages/django/db/models/base.py | 92 |
| `__delattr__` | `(self, name, /)` | <p>Implement delattr(self, name).</p> |  |  |
| `__dir__` | `(self, /)` | <p>Default dir() implementation.</p> |  |  |
| `__eq__` | `(self, other)` | <p>Return self==value.</p> | python3.13/site-packages/django/db/models/base.py | 593 |
| `__format__` | `(self, format_spec, /)` | <p>Default object formatter.</p><p>Return str(self) if format\_spec is empty. Raise TypeError otherwise.</p> |  |  |
| `__ge__` | `(self, value, /)` | <p>Return self>=value.</p> |  |  |
| `__getattribute__` | `(self, name, /)` | <p>Return getattr(self, name).</p> |  |  |
| `__getstate__` | `(self)` | <p>Hook to allow choosing the attributes to pickle.</p> | python3.13/site-packages/django/db/models/base.py | 614 |
| `__gt__` | `(self, value, /)` | <p>Return self>value.</p> |  |  |
| `__hash__` | `(self)` | <p>Return hash(self).</p> | python3.13/site-packages/django/db/models/base.py | 603 |
| `__init__` | `(self, *args, **kwargs)` | <p>Initialize self.  See help(type(self)) for accurate signature.</p> | python3.13/site-packages/django/db/models/base.py | 460 |
| `__init_subclass__` | `(**kwargs)` | <p>This method is called when a class is subclassed.</p><p>The default implementation does nothing. It may be<br>overridden to extend subclasses.</p> | python3.13/site-packages/django/db/models/utils.py | 60 |
| `__le__` | `(self, value, /)` | <p>Return self<=value.</p> |  |  |
| `__lt__` | `(self, value, /)` | <p>Return self<value.</p> |  |  |
| `__ne__` | `(self, value, /)` | <p>Return self!=value.</p> |  |  |
| `__new__` | `(*args, **kwargs)` | <p>Create and return a new object.  See help(type) for accurate signature.</p> |  |  |
| `__reduce__` | `(self)` | <p>Helper for pickle.</p> | python3.13/site-packages/django/db/models/base.py | 608 |
| `__reduce_ex__` | `(self, protocol, /)` | <p>Helper for pickle.</p> |  |  |
| `__repr__` | `(self)` | <p>Return repr(self).</p> | python3.13/site-packages/django/db/models/base.py | 587 |
| `__setattr__` | `(self, name, value, /)` | <p>Implement setattr(self, name, value).</p> |  |  |
| `__setstate__` | `(self, state)` |  | python3.13/site-packages/django/db/models/base.py | 631 |
| `__sizeof__` | `(self, /)` | <p>Size of object in memory, in bytes.</p> |  |  |
| `__str__` | `(self)` | <p>Return str(self).</p> | python3.13/site-packages/django/db/models/base.py | 590 |
| `__subclasshook__` | `(object, /)` | <p>Abstract classes can override this to customize issubclass().</p><p>This is invoked early on by abc.ABCMeta.\_\_subclasscheck\_\_().<br>It should return True, False or NotImplemented.  If it returns<br>NotImplemented, the normal algorithm is used.  Otherwise, it<br>overrides the normal algorithm (and the outcome is cached).</p> |  |  |


### Common Django Methods

| Method Name | Signature | Docstring | File | Line Number |
|-----------|---------|---------|----|-----------|
| `_check_column_name_clashes` | `()` |  | python3.13/site-packages/django/db/models/base.py | 1955 |
| `_check_constraints` | `(databases)` |  | python3.13/site-packages/django/db/models/base.py | 2420 |
| `_check_db_table_comment` | `(databases)` |  | python3.13/site-packages/django/db/models/base.py | 1749 |
| `_check_default_pk` | `()` |  | python3.13/site-packages/django/db/models/base.py | 1717 |
| `_check_field_name_clashes` | `()` | <p>Forbid field shadowing in multi-table inheritance.</p> | python3.13/site-packages/django/db/models/base.py | 1885 |
| `_check_fields` | `(**kwargs)` | <p>Perform all field checks.</p> | python3.13/site-packages/django/db/models/base.py | 1820 |
| `_check_id_field` | `()` | <p>Check if `id` field is a primary key.</p> | python3.13/site-packages/django/db/models/base.py | 1866 |
| `_check_indexes` | `(databases)` | <p>Check fields, names, and conditions of indexes.</p> | python3.13/site-packages/django/db/models/base.py | 2069 |
| `_check_local_fields` | `(fields, option)` |  | python3.13/site-packages/django/db/models/base.py | 2160 |
| `_check_long_column_names` | `(databases)` | <p>Check that any auto-generated column names are shorter than the limits<br>for each database in which the model will be created.</p> | python3.13/site-packages/django/db/models/base.py | 2324 |
| `_check_m2m_through_same_relationship` | `()` | <p>Check if no relationship model is used by more than one m2m field.</p> | python3.13/site-packages/django/db/models/base.py | 1830 |
| `_check_managers` | `(**kwargs)` | <p>Perform all manager checks.</p> | python3.13/site-packages/django/db/models/base.py | 1812 |
| `_check_model` | `()` |  | python3.13/site-packages/django/db/models/base.py | 1799 |
| `_check_model_name_db_lookup_clashes` | `()` |  | python3.13/site-packages/django/db/models/base.py | 1980 |
| `_check_ordering` | `()` | <p>Check "ordering" option -- is it a list of strings and do all fields<br>exist?</p> | python3.13/site-packages/django/db/models/base.py | 2215 |
| `_check_property_name_related_field_accessor_clashes` | `()` |  | python3.13/site-packages/django/db/models/base.py | 2004 |
| `_check_single_primary_key` | `()` |  | python3.13/site-packages/django/db/models/base.py | 2025 |
| `_check_swappable` | `()` | <p>Check if the swapped model exists.</p> | python3.13/site-packages/django/db/models/base.py | 1772 |
| `_check_unique_together` | `()` | <p>Check the value of "unique\_together" option.</p> | python3.13/site-packages/django/db/models/base.py | 2039 |
| `_do_insert` | `(self, manager, using, fields, returning_fields, raw)` | <p>Do an INSERT. If returning\_fields is defined then this method should<br>return the newly created data for the model.</p> | python3.13/site-packages/django/db/models/base.py | 1196 |
| `_do_update` | `(self, base_qs, using, pk_val, values, update_fields, forced_update)` | <p>Try to update the model. Return True if the model was updated (if an<br>update query was done and a matching row was found in the DB).</p> | python3.13/site-packages/django/db/models/base.py | 1168 |
| `_get_FIELD_display` | `(self, field)` |  | python3.13/site-packages/django/db/models/base.py | 1284 |
| `_get_expr_references` | `(expr)` |  | python3.13/site-packages/django/db/models/base.py | 2404 |
| `_get_field_expression_map` | `(self, meta, exclude=None)` |  | python3.13/site-packages/django/db/models/base.py | 1336 |
| `_get_next_or_previous_by_FIELD` | `(self, field, is_next, **kwargs)` |  | python3.13/site-packages/django/db/models/base.py | 1292 |
| `_get_next_or_previous_in_order` | `(self, is_next)` |  | python3.13/site-packages/django/db/models/base.py | 1313 |
| `_get_pk_val` | `(self, meta=None)` |  | python3.13/site-packages/django/db/models/base.py | 653 |
| `_get_unique_checks` | `(self, exclude=None, include_meta_constraints=False)` | <p>Return a list of checks to perform. Since validate\_unique() could be<br>called from a ModelForm, some fields may have been excluded; we can't<br>perform a unique check on a model that is missing fields involved<br>in that check. Fields that did not validate should also be excluded,<br>but they need to be passed in via the exclude argument.</p> | python3.13/site-packages/django/db/models/base.py | 1386 |
| `_parse_params` | `(self, *args, method_name, **kwargs)` |  | python3.13/site-packages/django/db/models/base.py | 780 |
| `_perform_date_checks` | `(self, date_checks)` |  | python3.13/site-packages/django/db/models/base.py | 1498 |
| `_perform_unique_checks` | `(self, unique_checks)` |  | python3.13/site-packages/django/db/models/base.py | 1449 |
| `_prepare_related_fields_for_save` | `(self, operation_name, fields=None)` |  | python3.13/site-packages/django/db/models/base.py | 1209 |
| `_save_parents` | `(self, cls, using, update_fields, force_insert, updated_parents=None)` | <p>Save all the parents of cls using values from self.</p> | python3.13/site-packages/django/db/models/base.py | 1023 |
| `_save_table` | `(self, raw=False, cls=None, force_insert=False, force_update=False, using=None, update_fields=None)` | <p>Do the heavy-lifting involved in saving. Update or insert the data<br>for a single table.</p> | python3.13/site-packages/django/db/models/base.py | 1070 |
| `_set_pk_val` | `(self, value)` |  | python3.13/site-packages/django/db/models/base.py | 657 |
| `_validate_force_insert` | `(force_insert)` |  | python3.13/site-packages/django/db/models/base.py | 931 |
| `adelete` | `(self, using=None, keep_parents=False)` |  | python3.13/site-packages/django/db/models/base.py | 1276 |
| `arefresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |  | python3.13/site-packages/django/db/models/base.py | 757 |
| `asave` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |  | python3.13/site-packages/django/db/models/base.py | 904 |
| `check` | `(**kwargs)` |  | python3.13/site-packages/django/db/models/base.py | 1680 |
| `clean` | `(self)` | <p>Hook for doing any extra model-wide validation after clean() has been<br>called on every field by self.clean\_fields. Any ValidationError raised<br>by this method will not be associated with a particular field; it will<br>have a special-case association with the field defined by NON\_FIELD\_ERRORS.</p> | python3.13/site-packages/django/db/models/base.py | 1361 |
| `clean_fields` | `(self, exclude=None)` | <p>Clean all fields and raise a ValidationError containing a dict<br>of all validation errors if any occur.</p> | python3.13/site-packages/django/db/models/base.py | 1652 |
| `date_error_message` | `(self, lookup_type, field_name, unique_for)` |  | python3.13/site-packages/django/db/models/base.py | 1529 |
| `delete` | `(self, using=None, keep_parents=False)` |  | python3.13/site-packages/django/db/models/base.py | 1263 |
| `from_db` | `(db, field_names, values)` |  | python3.13/site-packages/django/db/models/base.py | 574 |
| `full_clean` | `(self, exclude=None, validate_unique=True, validate_constraints=True)` | <p>Call clean\_fields(), clean(), validate\_unique(), and<br>validate\_constraints() on the model. Raise a ValidationError for any<br>errors that occur.</p> | python3.13/site-packages/django/db/models/base.py | 1605 |
| `get_constraints` | `(self)` |  | python3.13/site-packages/django/db/models/base.py | 1578 |
| `get_deferred_fields` | `(self)` | <p>Return a set containing names of deferred fields for this instance.</p> | python3.13/site-packages/django/db/models/base.py | 665 |
| `prepare_database_save` | `(self, field)` |  | python3.13/site-packages/django/db/models/base.py | 1354 |
| `refresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` | <p>Reload field values from the database.</p><p>By default, the reloading happens from the database this instance was<br>loaded from, or by the read router if this instance wasn't loaded from<br>any database. The using parameter will override the default.</p><p>Fields can be used to specify which fields to reload. The fields<br>should be an iterable of field attnames. If fields is None, then<br>all non-deferred fields are reloaded.</p><p>When accessing deferred fields of an instance, the deferred loading<br>of the field will call this method.</p> | python3.13/site-packages/django/db/models/base.py | 675 |
| `save` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` | <p>Save the current instance. Override this in a subclass if you want to<br>control the saving process.</p><p>The 'force\_insert' and 'force\_update' parameters can be used to insist<br>that the "save" must be an SQL insert or update (or equivalent for<br>non-SQL backends), respectively. Normally, they should not be set.</p> | python3.13/site-packages/django/db/models/base.py | 820 |
| `save_base` | `(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None)` | <p>Handle the parts of saving which should be done only once per save,<br>yet need to be done in raw saves, too. This includes some sanity<br>checks and signal sending.</p><p>The 'raw' argument is telling save\_base not to save any parent<br>models and not to do any changes to the values before save. This<br>is used by fixture loading.</p> | python3.13/site-packages/django/db/models/base.py | 951 |
| `serializable_value` | `(self, field_name)` | <p>Return the value of the field name for this instance. If the field is<br>a foreign key, return the id value instead of the object. If there's<br>no Field object with this name on the model, return the model<br>attribute's value.</p><p>Used to serialize a field's value (in the serializer, or form output,<br>for example). Normally, you would just access the attribute directly<br>and not use this method.</p> | python3.13/site-packages/django/db/models/base.py | 762 |
| `unique_error_message` | `(self, model_class, unique_check)` |  | python3.13/site-packages/django/db/models/base.py | 1546 |
| `validate_constraints` | `(self, exclude=None)` |  | python3.13/site-packages/django/db/models/base.py | 1585 |
| `validate_unique` | `(self, exclude=None)` | <p>Check unique constraints on the model and raise ValidationError if any<br>failed.</p> | python3.13/site-packages/django/db/models/base.py | 1370 |


---

# sales.BankAccount

## Model Info

| Key | Value |
|---|-----|
| Model Name | BankAccount |
| Verbose Name | bank account |
| Verbose Name Plural | bank accounts |
| Docstring | <p>Bank account payment method.</p> |
| Is Abstract | False |
| Is Proxy | False |
| Is Managed | True |
| Ordering | [] |
| Permissions | [] |
| Default Permissions | ('add', 'change', 'delete', 'view') |
| Indexes | [] |
| Constraints | [] |
| Database Table | sales_bankaccount |
| Base Manager | None |
| Default Manager | None |
| File | /home/watervize/omenapps_packages/django-model-info/example_project/sales/models.py |
| Starting Line Number | 44 |
| Method Resolution Order | (<class 'example_project.sales.models.BankAccount'>, <class 'example_project.sales.models.PaymentMethod'>, <class 'example_project.common.models.BaseModel'>, <class 'django.db.models.base.Model'>, <class 'django.db.models.utils.AltersData'>, <class 'object'>) |

## Fields

| Field Name | Field Type | Database Column | Database Type | Verbose Name |
|----------|----------|---------------|-------------|------------|
| `account_number` | CharField | account_number | varchar(50) | account number |
| `account_type` | CharField | account_type | varchar(20) | account type |
| `created_at` | DateTimeField | created_at | datetime | created at |
| `customer` | ForeignKey | customer_id | bigint | customer |
| `id (pk)` | BigAutoField | id | integer | ID |
| `is_active` | BooleanField | is_active | bool | is active |
| `is_default` | BooleanField | is_default | bool | is default |
| `name` | CharField | name | varchar(100) | name |
| `routing_number` | CharField | routing_number | varchar(20) | routing number |
| `updated_at` | DateTimeField | updated_at | datetime | updated at |

## Relations

| Field Name | Field Type | Database Column | Database Type | Related Model | Related Name |
|----------|----------|---------------|-------------|-------------|------------|
| `customer` | ForeignKey | customer_id | bigint | common.Customer | sales_bankaccount_related |

## Methods

### Other Methods

| Method Name | Signature | Docstring | File | Line Number |
|-----------|---------|---------|----|-----------|
| `activate` | `(self)` | <p>Activate the record</p> | watervize/omenapps_packages/django-model-info/example_project/common/models.py | 24 |
| `deactivate` | `(self)` | <p>Deactivate the record</p> | watervize/omenapps_packages/django-model-info/example_project/common/models.py | 29 |
| `get_next_by_created_at` | `(self, *, field=<django.db.models.fields.DateTimeField: created_at>, is_next=True, **kwargs)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |
| `get_next_by_updated_at` | `(self, *, field=<django.db.models.fields.DateTimeField: updated_at>, is_next=True, **kwargs)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |
| `get_previous_by_created_at` | `(self, *, field=<django.db.models.fields.DateTimeField: created_at>, is_next=False, **kwargs)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |
| `get_previous_by_updated_at` | `(self, *, field=<django.db.models.fields.DateTimeField: updated_at>, is_next=False, **kwargs)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |


### Dunder Methods

| Method Name | Signature | Docstring | File | Line Number |
|-----------|---------|---------|----|-----------|
| `__class__` | `(name, bases, attrs, **kwargs)` | <p>Metaclass for all models.</p> | python3.13/site-packages/django/db/models/base.py | 92 |
| `__delattr__` | `(self, name, /)` | <p>Implement delattr(self, name).</p> |  |  |
| `__dir__` | `(self, /)` | <p>Default dir() implementation.</p> |  |  |
| `__eq__` | `(self, other)` | <p>Return self==value.</p> | python3.13/site-packages/django/db/models/base.py | 593 |
| `__format__` | `(self, format_spec, /)` | <p>Default object formatter.</p><p>Return str(self) if format\_spec is empty. Raise TypeError otherwise.</p> |  |  |
| `__ge__` | `(self, value, /)` | <p>Return self>=value.</p> |  |  |
| `__getattribute__` | `(self, name, /)` | <p>Return getattr(self, name).</p> |  |  |
| `__getstate__` | `(self)` | <p>Hook to allow choosing the attributes to pickle.</p> | python3.13/site-packages/django/db/models/base.py | 614 |
| `__gt__` | `(self, value, /)` | <p>Return self>value.</p> |  |  |
| `__hash__` | `(self)` | <p>Return hash(self).</p> | python3.13/site-packages/django/db/models/base.py | 603 |
| `__init__` | `(self, *args, **kwargs)` | <p>Initialize self.  See help(type(self)) for accurate signature.</p> | python3.13/site-packages/django/db/models/base.py | 460 |
| `__init_subclass__` | `(**kwargs)` | <p>This method is called when a class is subclassed.</p><p>The default implementation does nothing. It may be<br>overridden to extend subclasses.</p> | python3.13/site-packages/django/db/models/utils.py | 60 |
| `__le__` | `(self, value, /)` | <p>Return self<=value.</p> |  |  |
| `__lt__` | `(self, value, /)` | <p>Return self<value.</p> |  |  |
| `__ne__` | `(self, value, /)` | <p>Return self!=value.</p> |  |  |
| `__new__` | `(*args, **kwargs)` | <p>Create and return a new object.  See help(type) for accurate signature.</p> |  |  |
| `__reduce__` | `(self)` | <p>Helper for pickle.</p> | python3.13/site-packages/django/db/models/base.py | 608 |
| `__reduce_ex__` | `(self, protocol, /)` | <p>Helper for pickle.</p> |  |  |
| `__repr__` | `(self)` | <p>Return repr(self).</p> | python3.13/site-packages/django/db/models/base.py | 587 |
| `__setattr__` | `(self, name, value, /)` | <p>Implement setattr(self, name, value).</p> |  |  |
| `__setstate__` | `(self, state)` |  | python3.13/site-packages/django/db/models/base.py | 631 |
| `__sizeof__` | `(self, /)` | <p>Size of object in memory, in bytes.</p> |  |  |
| `__str__` | `(self)` | <p>Return str(self).</p> | python3.13/site-packages/django/db/models/base.py | 590 |
| `__subclasshook__` | `(object, /)` | <p>Abstract classes can override this to customize issubclass().</p><p>This is invoked early on by abc.ABCMeta.\_\_subclasscheck\_\_().<br>It should return True, False or NotImplemented.  If it returns<br>NotImplemented, the normal algorithm is used.  Otherwise, it<br>overrides the normal algorithm (and the outcome is cached).</p> |  |  |


### Common Django Methods

| Method Name | Signature | Docstring | File | Line Number |
|-----------|---------|---------|----|-----------|
| `_check_column_name_clashes` | `()` |  | python3.13/site-packages/django/db/models/base.py | 1955 |
| `_check_constraints` | `(databases)` |  | python3.13/site-packages/django/db/models/base.py | 2420 |
| `_check_db_table_comment` | `(databases)` |  | python3.13/site-packages/django/db/models/base.py | 1749 |
| `_check_default_pk` | `()` |  | python3.13/site-packages/django/db/models/base.py | 1717 |
| `_check_field_name_clashes` | `()` | <p>Forbid field shadowing in multi-table inheritance.</p> | python3.13/site-packages/django/db/models/base.py | 1885 |
| `_check_fields` | `(**kwargs)` | <p>Perform all field checks.</p> | python3.13/site-packages/django/db/models/base.py | 1820 |
| `_check_id_field` | `()` | <p>Check if `id` field is a primary key.</p> | python3.13/site-packages/django/db/models/base.py | 1866 |
| `_check_indexes` | `(databases)` | <p>Check fields, names, and conditions of indexes.</p> | python3.13/site-packages/django/db/models/base.py | 2069 |
| `_check_local_fields` | `(fields, option)` |  | python3.13/site-packages/django/db/models/base.py | 2160 |
| `_check_long_column_names` | `(databases)` | <p>Check that any auto-generated column names are shorter than the limits<br>for each database in which the model will be created.</p> | python3.13/site-packages/django/db/models/base.py | 2324 |
| `_check_m2m_through_same_relationship` | `()` | <p>Check if no relationship model is used by more than one m2m field.</p> | python3.13/site-packages/django/db/models/base.py | 1830 |
| `_check_managers` | `(**kwargs)` | <p>Perform all manager checks.</p> | python3.13/site-packages/django/db/models/base.py | 1812 |
| `_check_model` | `()` |  | python3.13/site-packages/django/db/models/base.py | 1799 |
| `_check_model_name_db_lookup_clashes` | `()` |  | python3.13/site-packages/django/db/models/base.py | 1980 |
| `_check_ordering` | `()` | <p>Check "ordering" option -- is it a list of strings and do all fields<br>exist?</p> | python3.13/site-packages/django/db/models/base.py | 2215 |
| `_check_property_name_related_field_accessor_clashes` | `()` |  | python3.13/site-packages/django/db/models/base.py | 2004 |
| `_check_single_primary_key` | `()` |  | python3.13/site-packages/django/db/models/base.py | 2025 |
| `_check_swappable` | `()` | <p>Check if the swapped model exists.</p> | python3.13/site-packages/django/db/models/base.py | 1772 |
| `_check_unique_together` | `()` | <p>Check the value of "unique\_together" option.</p> | python3.13/site-packages/django/db/models/base.py | 2039 |
| `_do_insert` | `(self, manager, using, fields, returning_fields, raw)` | <p>Do an INSERT. If returning\_fields is defined then this method should<br>return the newly created data for the model.</p> | python3.13/site-packages/django/db/models/base.py | 1196 |
| `_do_update` | `(self, base_qs, using, pk_val, values, update_fields, forced_update)` | <p>Try to update the model. Return True if the model was updated (if an<br>update query was done and a matching row was found in the DB).</p> | python3.13/site-packages/django/db/models/base.py | 1168 |
| `_get_FIELD_display` | `(self, field)` |  | python3.13/site-packages/django/db/models/base.py | 1284 |
| `_get_expr_references` | `(expr)` |  | python3.13/site-packages/django/db/models/base.py | 2404 |
| `_get_field_expression_map` | `(self, meta, exclude=None)` |  | python3.13/site-packages/django/db/models/base.py | 1336 |
| `_get_next_or_previous_by_FIELD` | `(self, field, is_next, **kwargs)` |  | python3.13/site-packages/django/db/models/base.py | 1292 |
| `_get_next_or_previous_in_order` | `(self, is_next)` |  | python3.13/site-packages/django/db/models/base.py | 1313 |
| `_get_pk_val` | `(self, meta=None)` |  | python3.13/site-packages/django/db/models/base.py | 653 |
| `_get_unique_checks` | `(self, exclude=None, include_meta_constraints=False)` | <p>Return a list of checks to perform. Since validate\_unique() could be<br>called from a ModelForm, some fields may have been excluded; we can't<br>perform a unique check on a model that is missing fields involved<br>in that check. Fields that did not validate should also be excluded,<br>but they need to be passed in via the exclude argument.</p> | python3.13/site-packages/django/db/models/base.py | 1386 |
| `_parse_params` | `(self, *args, method_name, **kwargs)` |  | python3.13/site-packages/django/db/models/base.py | 780 |
| `_perform_date_checks` | `(self, date_checks)` |  | python3.13/site-packages/django/db/models/base.py | 1498 |
| `_perform_unique_checks` | `(self, unique_checks)` |  | python3.13/site-packages/django/db/models/base.py | 1449 |
| `_prepare_related_fields_for_save` | `(self, operation_name, fields=None)` |  | python3.13/site-packages/django/db/models/base.py | 1209 |
| `_save_parents` | `(self, cls, using, update_fields, force_insert, updated_parents=None)` | <p>Save all the parents of cls using values from self.</p> | python3.13/site-packages/django/db/models/base.py | 1023 |
| `_save_table` | `(self, raw=False, cls=None, force_insert=False, force_update=False, using=None, update_fields=None)` | <p>Do the heavy-lifting involved in saving. Update or insert the data<br>for a single table.</p> | python3.13/site-packages/django/db/models/base.py | 1070 |
| `_set_pk_val` | `(self, value)` |  | python3.13/site-packages/django/db/models/base.py | 657 |
| `_validate_force_insert` | `(force_insert)` |  | python3.13/site-packages/django/db/models/base.py | 931 |
| `adelete` | `(self, using=None, keep_parents=False)` |  | python3.13/site-packages/django/db/models/base.py | 1276 |
| `arefresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |  | python3.13/site-packages/django/db/models/base.py | 757 |
| `asave` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |  | python3.13/site-packages/django/db/models/base.py | 904 |
| `check` | `(**kwargs)` |  | python3.13/site-packages/django/db/models/base.py | 1680 |
| `clean` | `(self)` | <p>Hook for doing any extra model-wide validation after clean() has been<br>called on every field by self.clean\_fields. Any ValidationError raised<br>by this method will not be associated with a particular field; it will<br>have a special-case association with the field defined by NON\_FIELD\_ERRORS.</p> | python3.13/site-packages/django/db/models/base.py | 1361 |
| `clean_fields` | `(self, exclude=None)` | <p>Clean all fields and raise a ValidationError containing a dict<br>of all validation errors if any occur.</p> | python3.13/site-packages/django/db/models/base.py | 1652 |
| `date_error_message` | `(self, lookup_type, field_name, unique_for)` |  | python3.13/site-packages/django/db/models/base.py | 1529 |
| `delete` | `(self, using=None, keep_parents=False)` |  | python3.13/site-packages/django/db/models/base.py | 1263 |
| `from_db` | `(db, field_names, values)` |  | python3.13/site-packages/django/db/models/base.py | 574 |
| `full_clean` | `(self, exclude=None, validate_unique=True, validate_constraints=True)` | <p>Call clean\_fields(), clean(), validate\_unique(), and<br>validate\_constraints() on the model. Raise a ValidationError for any<br>errors that occur.</p> | python3.13/site-packages/django/db/models/base.py | 1605 |
| `get_constraints` | `(self)` |  | python3.13/site-packages/django/db/models/base.py | 1578 |
| `get_deferred_fields` | `(self)` | <p>Return a set containing names of deferred fields for this instance.</p> | python3.13/site-packages/django/db/models/base.py | 665 |
| `prepare_database_save` | `(self, field)` |  | python3.13/site-packages/django/db/models/base.py | 1354 |
| `refresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` | <p>Reload field values from the database.</p><p>By default, the reloading happens from the database this instance was<br>loaded from, or by the read router if this instance wasn't loaded from<br>any database. The using parameter will override the default.</p><p>Fields can be used to specify which fields to reload. The fields<br>should be an iterable of field attnames. If fields is None, then<br>all non-deferred fields are reloaded.</p><p>When accessing deferred fields of an instance, the deferred loading<br>of the field will call this method.</p> | python3.13/site-packages/django/db/models/base.py | 675 |
| `save` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` | <p>Save the current instance. Override this in a subclass if you want to<br>control the saving process.</p><p>The 'force\_insert' and 'force\_update' parameters can be used to insist<br>that the "save" must be an SQL insert or update (or equivalent for<br>non-SQL backends), respectively. Normally, they should not be set.</p> | python3.13/site-packages/django/db/models/base.py | 820 |
| `save_base` | `(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None)` | <p>Handle the parts of saving which should be done only once per save,<br>yet need to be done in raw saves, too. This includes some sanity<br>checks and signal sending.</p><p>The 'raw' argument is telling save\_base not to save any parent<br>models and not to do any changes to the values before save. This<br>is used by fixture loading.</p> | python3.13/site-packages/django/db/models/base.py | 951 |
| `serializable_value` | `(self, field_name)` | <p>Return the value of the field name for this instance. If the field is<br>a foreign key, return the id value instead of the object. If there's<br>no Field object with this name on the model, return the model<br>attribute's value.</p><p>Used to serialize a field's value (in the serializer, or form output,<br>for example). Normally, you would just access the attribute directly<br>and not use this method.</p> | python3.13/site-packages/django/db/models/base.py | 762 |
| `unique_error_message` | `(self, model_class, unique_check)` |  | python3.13/site-packages/django/db/models/base.py | 1546 |
| `validate_constraints` | `(self, exclude=None)` |  | python3.13/site-packages/django/db/models/base.py | 1585 |
| `validate_unique` | `(self, exclude=None)` | <p>Check unique constraints on the model and raise ValidationError if any<br>failed.</p> | python3.13/site-packages/django/db/models/base.py | 1370 |


---

# sales.ShippingAddress

## Model Info

| Key | Value |
|---|-----|
| Model Name | ShippingAddress |
| Verbose Name | shipping address |
| Verbose Name Plural | shipping addresses |
| Docstring | <p>Shipping address model for customer orders.</p><p>Tracks both customer's saved addresses and one-off order addresses.</p> |
| Is Abstract | False |
| Is Proxy | False |
| Is Managed | True |
| Ordering | [] |
| Permissions | [] |
| Default Permissions | ('add', 'change', 'delete', 'view') |
| Indexes | [<Index: fields=['customer', 'is_default'] name='sales_shipp_custome_2b1495_idx'>, <Index: fields=['postal_code', 'city'] name='sales_shipp_postal__4bc8fc_idx'>] |
| Constraints | [<CheckConstraint: condition=(AND: ('street_address1__isnull', False), (NOT (AND: ('street_address1', '')))) name='required_street_address'>] |
| Database Table | sales_shippingaddress |
| Base Manager | None |
| Default Manager | None |
| File | /home/watervize/omenapps_packages/django-model-info/example_project/sales/models.py |
| Starting Line Number | 52 |
| Method Resolution Order | (<class 'example_project.sales.models.ShippingAddress'>, <class 'example_project.common.models.BaseModel'>, <class 'django.db.models.base.Model'>, <class 'django.db.models.utils.AltersData'>, <class 'object'>) |

## Fields

| Field Name | Field Type | Database Column | Database Type | Verbose Name |
|----------|----------|---------------|-------------|------------|
| `city` | CharField | city | varchar(100) | city |
| `country` | CharField | country | varchar(100) | country |
| `created_at` | DateTimeField | created_at | datetime | created at |
| `customer` | ForeignKey | customer_id | bigint | customer |
| `delivery_instructions` | TextField | delivery_instructions | text | delivery instructions |
| `id (pk)` | BigAutoField | id | integer | ID |
| `is_active` | BooleanField | is_active | bool | is active |
| `is_default` | BooleanField | is_default | bool | is default |
| `name` | CharField | name | varchar(200) | name |
| `order` | ManyToOneRel |  | bigint |  |
| `phone` | CharField | phone | varchar(20) | phone |
| `postal_code` | CharField | postal_code | varchar(20) | postal code |
| `state` | CharField | state | varchar(100) | state |
| `street_address1` | CharField | street_address1 | varchar(200) | street address1 |
| `street_address2` | CharField | street_address2 | varchar(200) | street address2 |
| `updated_at` | DateTimeField | updated_at | datetime | updated at |

## Relations

| Field Name | Field Type | Database Column | Database Type | Related Model | Related Name |
|----------|----------|---------------|-------------|-------------|------------|
| `customer` | ForeignKey | customer_id | bigint | common.Customer | shipping_addresses |

## Methods

### Other Methods

| Method Name | Signature | Docstring | File | Line Number |
|-----------|---------|---------|----|-----------|
| `activate` | `(self)` | <p>Activate the record</p> | watervize/omenapps_packages/django-model-info/example_project/common/models.py | 24 |
| `deactivate` | `(self)` | <p>Deactivate the record</p> | watervize/omenapps_packages/django-model-info/example_project/common/models.py | 29 |
| `get_next_by_created_at` | `(self, *, field=<django.db.models.fields.DateTimeField: created_at>, is_next=True, **kwargs)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |
| `get_next_by_updated_at` | `(self, *, field=<django.db.models.fields.DateTimeField: updated_at>, is_next=True, **kwargs)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |
| `get_previous_by_created_at` | `(self, *, field=<django.db.models.fields.DateTimeField: created_at>, is_next=False, **kwargs)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |
| `get_previous_by_updated_at` | `(self, *, field=<django.db.models.fields.DateTimeField: updated_at>, is_next=False, **kwargs)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |


### Private Methods

| Method Name | Signature | Docstring | File | Line Number |
|-----------|---------|---------|----|-----------|
| `_get_address_parts` | `(self)` | <p>Return address parts as a list.</p> | watervize/omenapps_packages/django-model-info/example_project/sales/models.py | 90 |


### Dunder Methods

| Method Name | Signature | Docstring | File | Line Number |
|-----------|---------|---------|----|-----------|
| `__class__` | `(name, bases, attrs, **kwargs)` | <p>Metaclass for all models.</p> | python3.13/site-packages/django/db/models/base.py | 92 |
| `__delattr__` | `(self, name, /)` | <p>Implement delattr(self, name).</p> |  |  |
| `__dir__` | `(self, /)` | <p>Default dir() implementation.</p> |  |  |
| `__eq__` | `(self, other)` | <p>Return self==value.</p> | python3.13/site-packages/django/db/models/base.py | 593 |
| `__format__` | `(self, format_spec, /)` | <p>Default object formatter.</p><p>Return str(self) if format\_spec is empty. Raise TypeError otherwise.</p> |  |  |
| `__ge__` | `(self, value, /)` | <p>Return self>=value.</p> |  |  |
| `__getattribute__` | `(self, name, /)` | <p>Return getattr(self, name).</p> |  |  |
| `__getstate__` | `(self)` | <p>Hook to allow choosing the attributes to pickle.</p> | python3.13/site-packages/django/db/models/base.py | 614 |
| `__gt__` | `(self, value, /)` | <p>Return self>value.</p> |  |  |
| `__hash__` | `(self)` | <p>Return hash(self).</p> | python3.13/site-packages/django/db/models/base.py | 603 |
| `__init__` | `(self, *args, **kwargs)` | <p>Initialize self.  See help(type(self)) for accurate signature.</p> | python3.13/site-packages/django/db/models/base.py | 460 |
| `__init_subclass__` | `(**kwargs)` | <p>This method is called when a class is subclassed.</p><p>The default implementation does nothing. It may be<br>overridden to extend subclasses.</p> | python3.13/site-packages/django/db/models/utils.py | 60 |
| `__le__` | `(self, value, /)` | <p>Return self<=value.</p> |  |  |
| `__lt__` | `(self, value, /)` | <p>Return self<value.</p> |  |  |
| `__ne__` | `(self, value, /)` | <p>Return self!=value.</p> |  |  |
| `__new__` | `(*args, **kwargs)` | <p>Create and return a new object.  See help(type) for accurate signature.</p> |  |  |
| `__reduce__` | `(self)` | <p>Helper for pickle.</p> | python3.13/site-packages/django/db/models/base.py | 608 |
| `__reduce_ex__` | `(self, protocol, /)` | <p>Helper for pickle.</p> |  |  |
| `__repr__` | `(self)` | <p>Return repr(self).</p> | python3.13/site-packages/django/db/models/base.py | 587 |
| `__setattr__` | `(self, name, value, /)` | <p>Implement setattr(self, name, value).</p> |  |  |
| `__setstate__` | `(self, state)` |  | python3.13/site-packages/django/db/models/base.py | 631 |
| `__sizeof__` | `(self, /)` | <p>Size of object in memory, in bytes.</p> |  |  |
| `__str__` | `(self)` | <p>Return str(self).</p> | watervize/omenapps_packages/django-model-info/example_project/sales/models.py | 79 |
| `__subclasshook__` | `(object, /)` | <p>Abstract classes can override this to customize issubclass().</p><p>This is invoked early on by abc.ABCMeta.\_\_subclasscheck\_\_().<br>It should return True, False or NotImplemented.  If it returns<br>NotImplemented, the normal algorithm is used.  Otherwise, it<br>overrides the normal algorithm (and the outcome is cached).</p> |  |  |


### Common Django Methods

| Method Name | Signature | Docstring | File | Line Number |
|-----------|---------|---------|----|-----------|
| `_check_column_name_clashes` | `()` |  | python3.13/site-packages/django/db/models/base.py | 1955 |
| `_check_constraints` | `(databases)` |  | python3.13/site-packages/django/db/models/base.py | 2420 |
| `_check_db_table_comment` | `(databases)` |  | python3.13/site-packages/django/db/models/base.py | 1749 |
| `_check_default_pk` | `()` |  | python3.13/site-packages/django/db/models/base.py | 1717 |
| `_check_field_name_clashes` | `()` | <p>Forbid field shadowing in multi-table inheritance.</p> | python3.13/site-packages/django/db/models/base.py | 1885 |
| `_check_fields` | `(**kwargs)` | <p>Perform all field checks.</p> | python3.13/site-packages/django/db/models/base.py | 1820 |
| `_check_id_field` | `()` | <p>Check if `id` field is a primary key.</p> | python3.13/site-packages/django/db/models/base.py | 1866 |
| `_check_indexes` | `(databases)` | <p>Check fields, names, and conditions of indexes.</p> | python3.13/site-packages/django/db/models/base.py | 2069 |
| `_check_local_fields` | `(fields, option)` |  | python3.13/site-packages/django/db/models/base.py | 2160 |
| `_check_long_column_names` | `(databases)` | <p>Check that any auto-generated column names are shorter than the limits<br>for each database in which the model will be created.</p> | python3.13/site-packages/django/db/models/base.py | 2324 |
| `_check_m2m_through_same_relationship` | `()` | <p>Check if no relationship model is used by more than one m2m field.</p> | python3.13/site-packages/django/db/models/base.py | 1830 |
| `_check_managers` | `(**kwargs)` | <p>Perform all manager checks.</p> | python3.13/site-packages/django/db/models/base.py | 1812 |
| `_check_model` | `()` |  | python3.13/site-packages/django/db/models/base.py | 1799 |
| `_check_model_name_db_lookup_clashes` | `()` |  | python3.13/site-packages/django/db/models/base.py | 1980 |
| `_check_ordering` | `()` | <p>Check "ordering" option -- is it a list of strings and do all fields<br>exist?</p> | python3.13/site-packages/django/db/models/base.py | 2215 |
| `_check_property_name_related_field_accessor_clashes` | `()` |  | python3.13/site-packages/django/db/models/base.py | 2004 |
| `_check_single_primary_key` | `()` |  | python3.13/site-packages/django/db/models/base.py | 2025 |
| `_check_swappable` | `()` | <p>Check if the swapped model exists.</p> | python3.13/site-packages/django/db/models/base.py | 1772 |
| `_check_unique_together` | `()` | <p>Check the value of "unique\_together" option.</p> | python3.13/site-packages/django/db/models/base.py | 2039 |
| `_do_insert` | `(self, manager, using, fields, returning_fields, raw)` | <p>Do an INSERT. If returning\_fields is defined then this method should<br>return the newly created data for the model.</p> | python3.13/site-packages/django/db/models/base.py | 1196 |
| `_do_update` | `(self, base_qs, using, pk_val, values, update_fields, forced_update)` | <p>Try to update the model. Return True if the model was updated (if an<br>update query was done and a matching row was found in the DB).</p> | python3.13/site-packages/django/db/models/base.py | 1168 |
| `_get_FIELD_display` | `(self, field)` |  | python3.13/site-packages/django/db/models/base.py | 1284 |
| `_get_expr_references` | `(expr)` |  | python3.13/site-packages/django/db/models/base.py | 2404 |
| `_get_field_expression_map` | `(self, meta, exclude=None)` |  | python3.13/site-packages/django/db/models/base.py | 1336 |
| `_get_next_or_previous_by_FIELD` | `(self, field, is_next, **kwargs)` |  | python3.13/site-packages/django/db/models/base.py | 1292 |
| `_get_next_or_previous_in_order` | `(self, is_next)` |  | python3.13/site-packages/django/db/models/base.py | 1313 |
| `_get_pk_val` | `(self, meta=None)` |  | python3.13/site-packages/django/db/models/base.py | 653 |
| `_get_unique_checks` | `(self, exclude=None, include_meta_constraints=False)` | <p>Return a list of checks to perform. Since validate\_unique() could be<br>called from a ModelForm, some fields may have been excluded; we can't<br>perform a unique check on a model that is missing fields involved<br>in that check. Fields that did not validate should also be excluded,<br>but they need to be passed in via the exclude argument.</p> | python3.13/site-packages/django/db/models/base.py | 1386 |
| `_parse_params` | `(self, *args, method_name, **kwargs)` |  | python3.13/site-packages/django/db/models/base.py | 780 |
| `_perform_date_checks` | `(self, date_checks)` |  | python3.13/site-packages/django/db/models/base.py | 1498 |
| `_perform_unique_checks` | `(self, unique_checks)` |  | python3.13/site-packages/django/db/models/base.py | 1449 |
| `_prepare_related_fields_for_save` | `(self, operation_name, fields=None)` |  | python3.13/site-packages/django/db/models/base.py | 1209 |
| `_save_parents` | `(self, cls, using, update_fields, force_insert, updated_parents=None)` | <p>Save all the parents of cls using values from self.</p> | python3.13/site-packages/django/db/models/base.py | 1023 |
| `_save_table` | `(self, raw=False, cls=None, force_insert=False, force_update=False, using=None, update_fields=None)` | <p>Do the heavy-lifting involved in saving. Update or insert the data<br>for a single table.</p> | python3.13/site-packages/django/db/models/base.py | 1070 |
| `_set_pk_val` | `(self, value)` |  | python3.13/site-packages/django/db/models/base.py | 657 |
| `_validate_force_insert` | `(force_insert)` |  | python3.13/site-packages/django/db/models/base.py | 931 |
| `adelete` | `(self, using=None, keep_parents=False)` |  | python3.13/site-packages/django/db/models/base.py | 1276 |
| `arefresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |  | python3.13/site-packages/django/db/models/base.py | 757 |
| `asave` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |  | python3.13/site-packages/django/db/models/base.py | 904 |
| `check` | `(**kwargs)` |  | python3.13/site-packages/django/db/models/base.py | 1680 |
| `clean` | `(self)` | <p>Hook for doing any extra model-wide validation after clean() has been<br>called on every field by self.clean\_fields. Any ValidationError raised<br>by this method will not be associated with a particular field; it will<br>have a special-case association with the field defined by NON\_FIELD\_ERRORS.</p> | python3.13/site-packages/django/db/models/base.py | 1361 |
| `clean_fields` | `(self, exclude=None)` | <p>Clean all fields and raise a ValidationError containing a dict<br>of all validation errors if any occur.</p> | python3.13/site-packages/django/db/models/base.py | 1652 |
| `date_error_message` | `(self, lookup_type, field_name, unique_for)` |  | python3.13/site-packages/django/db/models/base.py | 1529 |
| `delete` | `(self, using=None, keep_parents=False)` |  | python3.13/site-packages/django/db/models/base.py | 1263 |
| `from_db` | `(db, field_names, values)` |  | python3.13/site-packages/django/db/models/base.py | 574 |
| `full_clean` | `(self, exclude=None, validate_unique=True, validate_constraints=True)` | <p>Call clean\_fields(), clean(), validate\_unique(), and<br>validate\_constraints() on the model. Raise a ValidationError for any<br>errors that occur.</p> | python3.13/site-packages/django/db/models/base.py | 1605 |
| `get_constraints` | `(self)` |  | python3.13/site-packages/django/db/models/base.py | 1578 |
| `get_deferred_fields` | `(self)` | <p>Return a set containing names of deferred fields for this instance.</p> | python3.13/site-packages/django/db/models/base.py | 665 |
| `prepare_database_save` | `(self, field)` |  | python3.13/site-packages/django/db/models/base.py | 1354 |
| `refresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` | <p>Reload field values from the database.</p><p>By default, the reloading happens from the database this instance was<br>loaded from, or by the read router if this instance wasn't loaded from<br>any database. The using parameter will override the default.</p><p>Fields can be used to specify which fields to reload. The fields<br>should be an iterable of field attnames. If fields is None, then<br>all non-deferred fields are reloaded.</p><p>When accessing deferred fields of an instance, the deferred loading<br>of the field will call this method.</p> | python3.13/site-packages/django/db/models/base.py | 675 |
| `save` | `(self, *args, **kwargs)` | <p>Override save to ensure only one default address per customer.</p> | watervize/omenapps_packages/django-model-info/example_project/sales/models.py | 82 |
| `save_base` | `(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None)` | <p>Handle the parts of saving which should be done only once per save,<br>yet need to be done in raw saves, too. This includes some sanity<br>checks and signal sending.</p><p>The 'raw' argument is telling save\_base not to save any parent<br>models and not to do any changes to the values before save. This<br>is used by fixture loading.</p> | python3.13/site-packages/django/db/models/base.py | 951 |
| `serializable_value` | `(self, field_name)` | <p>Return the value of the field name for this instance. If the field is<br>a foreign key, return the id value instead of the object. If there's<br>no Field object with this name on the model, return the model<br>attribute's value.</p><p>Used to serialize a field's value (in the serializer, or form output,<br>for example). Normally, you would just access the attribute directly<br>and not use this method.</p> | python3.13/site-packages/django/db/models/base.py | 762 |
| `unique_error_message` | `(self, model_class, unique_check)` |  | python3.13/site-packages/django/db/models/base.py | 1546 |
| `validate_constraints` | `(self, exclude=None)` |  | python3.13/site-packages/django/db/models/base.py | 1585 |
| `validate_unique` | `(self, exclude=None)` | <p>Check unique constraints on the model and raise ValidationError if any<br>failed.</p> | python3.13/site-packages/django/db/models/base.py | 1370 |


---

# sales.Order

## Model Info

| Key | Value |
|---|-----|
| Model Name | Order |
| Verbose Name | order |
| Verbose Name Plural | orders |
| Docstring | <p>Order model representing customer purchases.</p><p>Args:<br>    customer: The customer who placed the order<br>    status: Current order status</p><p>Raises:<br>    ValidationError: If order total is negative</p> |
| Is Abstract | False |
| Is Proxy | False |
| Is Managed | True |
| Ordering | ['-order_date'] |
| Permissions | [] |
| Default Permissions | ('add', 'change', 'delete', 'view') |
| Indexes | [<Index: fields=['order_number', 'status'] name='sales_order_order_n_ecbdb4_idx'>, <Index: fields=['customer', '-order_date'] name='sales_order_custome_2bbc57_idx'>] |
| Constraints | [] |
| Database Table | sales_order |
| Base Manager | None |
| Default Manager | None |
| File | /home/watervize/omenapps_packages/django-model-info/example_project/sales/models.py |
| Starting Line Number | 132 |
| Method Resolution Order | (<class 'example_project.sales.models.Order'>, <class 'example_project.common.models.BaseModel'>, <class 'django.db.models.base.Model'>, <class 'django.db.models.utils.AltersData'>, <class 'object'>) |

## Fields

| Field Name | Field Type | Database Column | Database Type | Verbose Name |
|----------|----------|---------------|-------------|------------|
| `created_at` | DateTimeField | created_at | datetime | created at |
| `customer` | ForeignKey | customer_id | bigint | customer |
| `id (pk)` | BigAutoField | id | integer | ID |
| `is_active` | BooleanField | is_active | bool | is active |
| `items` | ManyToOneRel |  | bigint |  |
| `notes` | TextField | notes | text | notes |
| `order_date` | DateTimeField | order_date | datetime | order date |
| `order_number` | CharField | order_number | varchar(50) | order number |
| `shipping_address` | ForeignKey | shipping_address_id | bigint | shipping address |
| `status` | CharField | status | varchar(20) | status |
| `total_amount` | DecimalField | total_amount | decimal | total amount |
| `updated_at` | DateTimeField | updated_at | datetime | updated at |

## Relations

| Field Name | Field Type | Database Column | Database Type | Related Model | Related Name |
|----------|----------|---------------|-------------|-------------|------------|
| `customer` | ForeignKey | customer_id | bigint | common.Customer | orders |
| `shipping_address` | ForeignKey | shipping_address_id | bigint | sales.ShippingAddress | order_set |

## Methods

### Other Methods

| Method Name | Signature | Docstring | File | Line Number |
|-----------|---------|---------|----|-----------|
| `activate` | `(self)` | <p>Activate the record</p> | watervize/omenapps_packages/django-model-info/example_project/common/models.py | 24 |
| `deactivate` | `(self)` | <p>Deactivate the record</p> | watervize/omenapps_packages/django-model-info/example_project/common/models.py | 29 |
| `get_next_by_created_at` | `(self, *, field=<django.db.models.fields.DateTimeField: created_at>, is_next=True, **kwargs)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |
| `get_next_by_order_date` | `(self, *, field=<django.db.models.fields.DateTimeField: order_date>, is_next=True, **kwargs)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |
| `get_next_by_updated_at` | `(self, *, field=<django.db.models.fields.DateTimeField: updated_at>, is_next=True, **kwargs)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |
| `get_previous_by_created_at` | `(self, *, field=<django.db.models.fields.DateTimeField: created_at>, is_next=False, **kwargs)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |
| `get_previous_by_order_date` | `(self, *, field=<django.db.models.fields.DateTimeField: order_date>, is_next=False, **kwargs)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |
| `get_previous_by_updated_at` | `(self, *, field=<django.db.models.fields.DateTimeField: updated_at>, is_next=False, **kwargs)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |
| `get_status_display` | `(self, *, field=<django.db.models.fields.CharField: status>)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |


### Dunder Methods

| Method Name | Signature | Docstring | File | Line Number |
|-----------|---------|---------|----|-----------|
| `__class__` | `(name, bases, attrs, **kwargs)` | <p>Metaclass for all models.</p> | python3.13/site-packages/django/db/models/base.py | 92 |
| `__delattr__` | `(self, name, /)` | <p>Implement delattr(self, name).</p> |  |  |
| `__dir__` | `(self, /)` | <p>Default dir() implementation.</p> |  |  |
| `__eq__` | `(self, other)` | <p>Return self==value.</p> | python3.13/site-packages/django/db/models/base.py | 593 |
| `__format__` | `(self, format_spec, /)` | <p>Default object formatter.</p><p>Return str(self) if format\_spec is empty. Raise TypeError otherwise.</p> |  |  |
| `__ge__` | `(self, value, /)` | <p>Return self>=value.</p> |  |  |
| `__getattribute__` | `(self, name, /)` | <p>Return getattr(self, name).</p> |  |  |
| `__getstate__` | `(self)` | <p>Hook to allow choosing the attributes to pickle.</p> | python3.13/site-packages/django/db/models/base.py | 614 |
| `__gt__` | `(self, value, /)` | <p>Return self>value.</p> |  |  |
| `__hash__` | `(self)` | <p>Return hash(self).</p> | python3.13/site-packages/django/db/models/base.py | 603 |
| `__init__` | `(self, *args, **kwargs)` | <p>Initialize self.  See help(type(self)) for accurate signature.</p> | python3.13/site-packages/django/db/models/base.py | 460 |
| `__init_subclass__` | `(**kwargs)` | <p>This method is called when a class is subclassed.</p><p>The default implementation does nothing. It may be<br>overridden to extend subclasses.</p> | python3.13/site-packages/django/db/models/utils.py | 60 |
| `__le__` | `(self, value, /)` | <p>Return self<=value.</p> |  |  |
| `__lt__` | `(self, value, /)` | <p>Return self<value.</p> |  |  |
| `__ne__` | `(self, value, /)` | <p>Return self!=value.</p> |  |  |
| `__new__` | `(*args, **kwargs)` | <p>Create and return a new object.  See help(type) for accurate signature.</p> |  |  |
| `__reduce__` | `(self)` | <p>Helper for pickle.</p> | python3.13/site-packages/django/db/models/base.py | 608 |
| `__reduce_ex__` | `(self, protocol, /)` | <p>Helper for pickle.</p> |  |  |
| `__repr__` | `(self)` | <p>Return repr(self).</p> | python3.13/site-packages/django/db/models/base.py | 587 |
| `__setattr__` | `(self, name, value, /)` | <p>Implement setattr(self, name, value).</p> |  |  |
| `__setstate__` | `(self, state)` |  | python3.13/site-packages/django/db/models/base.py | 631 |
| `__sizeof__` | `(self, /)` | <p>Size of object in memory, in bytes.</p> |  |  |
| `__str__` | `(self)` | <p>Return str(self).</p> | watervize/omenapps_packages/django-model-info/example_project/sales/models.py | 167 |
| `__subclasshook__` | `(object, /)` | <p>Abstract classes can override this to customize issubclass().</p><p>This is invoked early on by abc.ABCMeta.\_\_subclasscheck\_\_().<br>It should return True, False or NotImplemented.  If it returns<br>NotImplemented, the normal algorithm is used.  Otherwise, it<br>overrides the normal algorithm (and the outcome is cached).</p> |  |  |


### Common Django Methods

| Method Name | Signature | Docstring | File | Line Number |
|-----------|---------|---------|----|-----------|
| `_check_column_name_clashes` | `()` |  | python3.13/site-packages/django/db/models/base.py | 1955 |
| `_check_constraints` | `(databases)` |  | python3.13/site-packages/django/db/models/base.py | 2420 |
| `_check_db_table_comment` | `(databases)` |  | python3.13/site-packages/django/db/models/base.py | 1749 |
| `_check_default_pk` | `()` |  | python3.13/site-packages/django/db/models/base.py | 1717 |
| `_check_field_name_clashes` | `()` | <p>Forbid field shadowing in multi-table inheritance.</p> | python3.13/site-packages/django/db/models/base.py | 1885 |
| `_check_fields` | `(**kwargs)` | <p>Perform all field checks.</p> | python3.13/site-packages/django/db/models/base.py | 1820 |
| `_check_id_field` | `()` | <p>Check if `id` field is a primary key.</p> | python3.13/site-packages/django/db/models/base.py | 1866 |
| `_check_indexes` | `(databases)` | <p>Check fields, names, and conditions of indexes.</p> | python3.13/site-packages/django/db/models/base.py | 2069 |
| `_check_local_fields` | `(fields, option)` |  | python3.13/site-packages/django/db/models/base.py | 2160 |
| `_check_long_column_names` | `(databases)` | <p>Check that any auto-generated column names are shorter than the limits<br>for each database in which the model will be created.</p> | python3.13/site-packages/django/db/models/base.py | 2324 |
| `_check_m2m_through_same_relationship` | `()` | <p>Check if no relationship model is used by more than one m2m field.</p> | python3.13/site-packages/django/db/models/base.py | 1830 |
| `_check_managers` | `(**kwargs)` | <p>Perform all manager checks.</p> | python3.13/site-packages/django/db/models/base.py | 1812 |
| `_check_model` | `()` |  | python3.13/site-packages/django/db/models/base.py | 1799 |
| `_check_model_name_db_lookup_clashes` | `()` |  | python3.13/site-packages/django/db/models/base.py | 1980 |
| `_check_ordering` | `()` | <p>Check "ordering" option -- is it a list of strings and do all fields<br>exist?</p> | python3.13/site-packages/django/db/models/base.py | 2215 |
| `_check_property_name_related_field_accessor_clashes` | `()` |  | python3.13/site-packages/django/db/models/base.py | 2004 |
| `_check_single_primary_key` | `()` |  | python3.13/site-packages/django/db/models/base.py | 2025 |
| `_check_swappable` | `()` | <p>Check if the swapped model exists.</p> | python3.13/site-packages/django/db/models/base.py | 1772 |
| `_check_unique_together` | `()` | <p>Check the value of "unique\_together" option.</p> | python3.13/site-packages/django/db/models/base.py | 2039 |
| `_do_insert` | `(self, manager, using, fields, returning_fields, raw)` | <p>Do an INSERT. If returning\_fields is defined then this method should<br>return the newly created data for the model.</p> | python3.13/site-packages/django/db/models/base.py | 1196 |
| `_do_update` | `(self, base_qs, using, pk_val, values, update_fields, forced_update)` | <p>Try to update the model. Return True if the model was updated (if an<br>update query was done and a matching row was found in the DB).</p> | python3.13/site-packages/django/db/models/base.py | 1168 |
| `_get_FIELD_display` | `(self, field)` |  | python3.13/site-packages/django/db/models/base.py | 1284 |
| `_get_expr_references` | `(expr)` |  | python3.13/site-packages/django/db/models/base.py | 2404 |
| `_get_field_expression_map` | `(self, meta, exclude=None)` |  | python3.13/site-packages/django/db/models/base.py | 1336 |
| `_get_next_or_previous_by_FIELD` | `(self, field, is_next, **kwargs)` |  | python3.13/site-packages/django/db/models/base.py | 1292 |
| `_get_next_or_previous_in_order` | `(self, is_next)` |  | python3.13/site-packages/django/db/models/base.py | 1313 |
| `_get_pk_val` | `(self, meta=None)` |  | python3.13/site-packages/django/db/models/base.py | 653 |
| `_get_unique_checks` | `(self, exclude=None, include_meta_constraints=False)` | <p>Return a list of checks to perform. Since validate\_unique() could be<br>called from a ModelForm, some fields may have been excluded; we can't<br>perform a unique check on a model that is missing fields involved<br>in that check. Fields that did not validate should also be excluded,<br>but they need to be passed in via the exclude argument.</p> | python3.13/site-packages/django/db/models/base.py | 1386 |
| `_parse_params` | `(self, *args, method_name, **kwargs)` |  | python3.13/site-packages/django/db/models/base.py | 780 |
| `_perform_date_checks` | `(self, date_checks)` |  | python3.13/site-packages/django/db/models/base.py | 1498 |
| `_perform_unique_checks` | `(self, unique_checks)` |  | python3.13/site-packages/django/db/models/base.py | 1449 |
| `_prepare_related_fields_for_save` | `(self, operation_name, fields=None)` |  | python3.13/site-packages/django/db/models/base.py | 1209 |
| `_save_parents` | `(self, cls, using, update_fields, force_insert, updated_parents=None)` | <p>Save all the parents of cls using values from self.</p> | python3.13/site-packages/django/db/models/base.py | 1023 |
| `_save_table` | `(self, raw=False, cls=None, force_insert=False, force_update=False, using=None, update_fields=None)` | <p>Do the heavy-lifting involved in saving. Update or insert the data<br>for a single table.</p> | python3.13/site-packages/django/db/models/base.py | 1070 |
| `_set_pk_val` | `(self, value)` |  | python3.13/site-packages/django/db/models/base.py | 657 |
| `_validate_force_insert` | `(force_insert)` |  | python3.13/site-packages/django/db/models/base.py | 931 |
| `adelete` | `(self, using=None, keep_parents=False)` |  | python3.13/site-packages/django/db/models/base.py | 1276 |
| `arefresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |  | python3.13/site-packages/django/db/models/base.py | 757 |
| `asave` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |  | python3.13/site-packages/django/db/models/base.py | 904 |
| `check` | `(**kwargs)` |  | python3.13/site-packages/django/db/models/base.py | 1680 |
| `clean` | `(self)` | <p>Validate order total amount.</p> | watervize/omenapps_packages/django-model-info/example_project/sales/models.py | 170 |
| `clean_fields` | `(self, exclude=None)` | <p>Clean all fields and raise a ValidationError containing a dict<br>of all validation errors if any occur.</p> | python3.13/site-packages/django/db/models/base.py | 1652 |
| `date_error_message` | `(self, lookup_type, field_name, unique_for)` |  | python3.13/site-packages/django/db/models/base.py | 1529 |
| `delete` | `(self, using=None, keep_parents=False)` |  | python3.13/site-packages/django/db/models/base.py | 1263 |
| `from_db` | `(db, field_names, values)` |  | python3.13/site-packages/django/db/models/base.py | 574 |
| `full_clean` | `(self, exclude=None, validate_unique=True, validate_constraints=True)` | <p>Call clean\_fields(), clean(), validate\_unique(), and<br>validate\_constraints() on the model. Raise a ValidationError for any<br>errors that occur.</p> | python3.13/site-packages/django/db/models/base.py | 1605 |
| `get_constraints` | `(self)` |  | python3.13/site-packages/django/db/models/base.py | 1578 |
| `get_deferred_fields` | `(self)` | <p>Return a set containing names of deferred fields for this instance.</p> | python3.13/site-packages/django/db/models/base.py | 665 |
| `prepare_database_save` | `(self, field)` |  | python3.13/site-packages/django/db/models/base.py | 1354 |
| `refresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` | <p>Reload field values from the database.</p><p>By default, the reloading happens from the database this instance was<br>loaded from, or by the read router if this instance wasn't loaded from<br>any database. The using parameter will override the default.</p><p>Fields can be used to specify which fields to reload. The fields<br>should be an iterable of field attnames. If fields is None, then<br>all non-deferred fields are reloaded.</p><p>When accessing deferred fields of an instance, the deferred loading<br>of the field will call this method.</p> | python3.13/site-packages/django/db/models/base.py | 675 |
| `save` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` | <p>Save the current instance. Override this in a subclass if you want to<br>control the saving process.</p><p>The 'force\_insert' and 'force\_update' parameters can be used to insist<br>that the "save" must be an SQL insert or update (or equivalent for<br>non-SQL backends), respectively. Normally, they should not be set.</p> | python3.13/site-packages/django/db/models/base.py | 820 |
| `save_base` | `(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None)` | <p>Handle the parts of saving which should be done only once per save,<br>yet need to be done in raw saves, too. This includes some sanity<br>checks and signal sending.</p><p>The 'raw' argument is telling save\_base not to save any parent<br>models and not to do any changes to the values before save. This<br>is used by fixture loading.</p> | python3.13/site-packages/django/db/models/base.py | 951 |
| `serializable_value` | `(self, field_name)` | <p>Return the value of the field name for this instance. If the field is<br>a foreign key, return the id value instead of the object. If there's<br>no Field object with this name on the model, return the model<br>attribute's value.</p><p>Used to serialize a field's value (in the serializer, or form output,<br>for example). Normally, you would just access the attribute directly<br>and not use this method.</p> | python3.13/site-packages/django/db/models/base.py | 762 |
| `unique_error_message` | `(self, model_class, unique_check)` |  | python3.13/site-packages/django/db/models/base.py | 1546 |
| `validate_constraints` | `(self, exclude=None)` |  | python3.13/site-packages/django/db/models/base.py | 1585 |
| `validate_unique` | `(self, exclude=None)` | <p>Check unique constraints on the model and raise ValidationError if any<br>failed.</p> | python3.13/site-packages/django/db/models/base.py | 1370 |


## Custom Managers

### default

**Class:** `OrderManager`

**Module:** `example_project.sales.models`

*Custom manager for the Order model.*

#### Custom Methods

##### `cancelled(self)`

*Return cancelled orders.*

##### `completed(self)`

*Return completed orders.*

##### `pending(self)`

*Return pending orders.*

#### Custom QuerySet

**Class:** `OrderQuerySet`

**Module:** `example_project.sales.models`

*Custom queryset methods for the Order model.*

##### Custom Methods

###### `cancelled(self)`

*Return cancelled orders.*

Defined in: `/home/watervize/omenapps_packages/django-model-info/example_project/sales/models.py`:`119`

###### `completed(self)`

*Return completed orders.*

Defined in: `/home/watervize/omenapps_packages/django-model-info/example_project/sales/models.py`:`115`

###### `pending(self)`

*Return pending orders.*

Defined in: `/home/watervize/omenapps_packages/django-model-info/example_project/sales/models.py`:`111`

### objects

**Class:** `OrderManager`

**Module:** `example_project.sales.models`

*Custom manager for the Order model.*

#### Custom Methods

##### `cancelled(self)`

*Return cancelled orders.*

##### `completed(self)`

*Return completed orders.*

##### `pending(self)`

*Return pending orders.*

#### Custom QuerySet

**Class:** `OrderQuerySet`

**Module:** `example_project.sales.models`

*Custom queryset methods for the Order model.*

##### Custom Methods

###### `cancelled(self)`

*Return cancelled orders.*

Defined in: `/home/watervize/omenapps_packages/django-model-info/example_project/sales/models.py`:`119`

###### `completed(self)`

*Return completed orders.*

Defined in: `/home/watervize/omenapps_packages/django-model-info/example_project/sales/models.py`:`115`

###### `pending(self)`

*Return pending orders.*

Defined in: `/home/watervize/omenapps_packages/django-model-info/example_project/sales/models.py`:`111`


---

# sales.OrderItem

## Model Info

| Key | Value |
|---|-----|
| Model Name | OrderItem |
| Verbose Name | order item |
| Verbose Name Plural | order items |
| Docstring | <p>Individual item within an order.</p> |
| Is Abstract | False |
| Is Proxy | False |
| Is Managed | True |
| Ordering | [] |
| Permissions | [] |
| Default Permissions | ('add', 'change', 'delete', 'view') |
| Indexes | [] |
| Constraints | [] |
| Database Table | sales_orderitem |
| Base Manager | None |
| Default Manager | None |
| File | /home/watervize/omenapps_packages/django-model-info/example_project/sales/models.py |
| Starting Line Number | 176 |
| Method Resolution Order | (<class 'example_project.sales.models.OrderItem'>, <class 'example_project.common.models.BaseModel'>, <class 'django.db.models.base.Model'>, <class 'django.db.models.utils.AltersData'>, <class 'object'>) |

## Fields

| Field Name | Field Type | Database Column | Database Type | Verbose Name |
|----------|----------|---------------|-------------|------------|
| `created_at` | DateTimeField | created_at | datetime | created at |
| `id (pk)` | BigAutoField | id | integer | ID |
| `is_active` | BooleanField | is_active | bool | is active |
| `order` | ForeignKey | order_id | bigint | order |
| `product` | ForeignKey | product_id | bigint | product |
| `quantity` | PositiveIntegerField | quantity | integer unsigned | quantity |
| `unit_price` | DecimalField | unit_price | decimal | unit price |
| `updated_at` | DateTimeField | updated_at | datetime | updated at |

## Relations

| Field Name | Field Type | Database Column | Database Type | Related Model | Related Name |
|----------|----------|---------------|-------------|-------------|------------|
| `order` | ForeignKey | order_id | bigint | sales.Order | items |
| `product` | ForeignKey | product_id | bigint | inventory.Product | orderitem_set |

## Methods

### Other Methods

| Method Name | Signature | Docstring | File | Line Number |
|-----------|---------|---------|----|-----------|
| `activate` | `(self)` | <p>Activate the record</p> | watervize/omenapps_packages/django-model-info/example_project/common/models.py | 24 |
| `deactivate` | `(self)` | <p>Deactivate the record</p> | watervize/omenapps_packages/django-model-info/example_project/common/models.py | 29 |
| `get_next_by_created_at` | `(self, *, field=<django.db.models.fields.DateTimeField: created_at>, is_next=True, **kwargs)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |
| `get_next_by_updated_at` | `(self, *, field=<django.db.models.fields.DateTimeField: updated_at>, is_next=True, **kwargs)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |
| `get_previous_by_created_at` | `(self, *, field=<django.db.models.fields.DateTimeField: created_at>, is_next=False, **kwargs)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |
| `get_previous_by_updated_at` | `(self, *, field=<django.db.models.fields.DateTimeField: updated_at>, is_next=False, **kwargs)` |  | uv/python/cpython-3.13.0-linux-x86_64-gnu/lib/python3.13/functools.py | 395 |


### Dunder Methods

| Method Name | Signature | Docstring | File | Line Number |
|-----------|---------|---------|----|-----------|
| `__class__` | `(name, bases, attrs, **kwargs)` | <p>Metaclass for all models.</p> | python3.13/site-packages/django/db/models/base.py | 92 |
| `__delattr__` | `(self, name, /)` | <p>Implement delattr(self, name).</p> |  |  |
| `__dir__` | `(self, /)` | <p>Default dir() implementation.</p> |  |  |
| `__eq__` | `(self, other)` | <p>Return self==value.</p> | python3.13/site-packages/django/db/models/base.py | 593 |
| `__format__` | `(self, format_spec, /)` | <p>Default object formatter.</p><p>Return str(self) if format\_spec is empty. Raise TypeError otherwise.</p> |  |  |
| `__ge__` | `(self, value, /)` | <p>Return self>=value.</p> |  |  |
| `__getattribute__` | `(self, name, /)` | <p>Return getattr(self, name).</p> |  |  |
| `__getstate__` | `(self)` | <p>Hook to allow choosing the attributes to pickle.</p> | python3.13/site-packages/django/db/models/base.py | 614 |
| `__gt__` | `(self, value, /)` | <p>Return self>value.</p> |  |  |
| `__hash__` | `(self)` | <p>Return hash(self).</p> | python3.13/site-packages/django/db/models/base.py | 603 |
| `__init__` | `(self, *args, **kwargs)` | <p>Initialize self.  See help(type(self)) for accurate signature.</p> | python3.13/site-packages/django/db/models/base.py | 460 |
| `__init_subclass__` | `(**kwargs)` | <p>This method is called when a class is subclassed.</p><p>The default implementation does nothing. It may be<br>overridden to extend subclasses.</p> | python3.13/site-packages/django/db/models/utils.py | 60 |
| `__le__` | `(self, value, /)` | <p>Return self<=value.</p> |  |  |
| `__lt__` | `(self, value, /)` | <p>Return self<value.</p> |  |  |
| `__ne__` | `(self, value, /)` | <p>Return self!=value.</p> |  |  |
| `__new__` | `(*args, **kwargs)` | <p>Create and return a new object.  See help(type) for accurate signature.</p> |  |  |
| `__reduce__` | `(self)` | <p>Helper for pickle.</p> | python3.13/site-packages/django/db/models/base.py | 608 |
| `__reduce_ex__` | `(self, protocol, /)` | <p>Helper for pickle.</p> |  |  |
| `__repr__` | `(self)` | <p>Return repr(self).</p> | python3.13/site-packages/django/db/models/base.py | 587 |
| `__setattr__` | `(self, name, value, /)` | <p>Implement setattr(self, name, value).</p> |  |  |
| `__setstate__` | `(self, state)` |  | python3.13/site-packages/django/db/models/base.py | 631 |
| `__sizeof__` | `(self, /)` | <p>Size of object in memory, in bytes.</p> |  |  |
| `__str__` | `(self)` | <p>Return str(self).</p> | python3.13/site-packages/django/db/models/base.py | 590 |
| `__subclasshook__` | `(object, /)` | <p>Abstract classes can override this to customize issubclass().</p><p>This is invoked early on by abc.ABCMeta.\_\_subclasscheck\_\_().<br>It should return True, False or NotImplemented.  If it returns<br>NotImplemented, the normal algorithm is used.  Otherwise, it<br>overrides the normal algorithm (and the outcome is cached).</p> |  |  |


### Common Django Methods

| Method Name | Signature | Docstring | File | Line Number |
|-----------|---------|---------|----|-----------|
| `_check_column_name_clashes` | `()` |  | python3.13/site-packages/django/db/models/base.py | 1955 |
| `_check_constraints` | `(databases)` |  | python3.13/site-packages/django/db/models/base.py | 2420 |
| `_check_db_table_comment` | `(databases)` |  | python3.13/site-packages/django/db/models/base.py | 1749 |
| `_check_default_pk` | `()` |  | python3.13/site-packages/django/db/models/base.py | 1717 |
| `_check_field_name_clashes` | `()` | <p>Forbid field shadowing in multi-table inheritance.</p> | python3.13/site-packages/django/db/models/base.py | 1885 |
| `_check_fields` | `(**kwargs)` | <p>Perform all field checks.</p> | python3.13/site-packages/django/db/models/base.py | 1820 |
| `_check_id_field` | `()` | <p>Check if `id` field is a primary key.</p> | python3.13/site-packages/django/db/models/base.py | 1866 |
| `_check_indexes` | `(databases)` | <p>Check fields, names, and conditions of indexes.</p> | python3.13/site-packages/django/db/models/base.py | 2069 |
| `_check_local_fields` | `(fields, option)` |  | python3.13/site-packages/django/db/models/base.py | 2160 |
| `_check_long_column_names` | `(databases)` | <p>Check that any auto-generated column names are shorter than the limits<br>for each database in which the model will be created.</p> | python3.13/site-packages/django/db/models/base.py | 2324 |
| `_check_m2m_through_same_relationship` | `()` | <p>Check if no relationship model is used by more than one m2m field.</p> | python3.13/site-packages/django/db/models/base.py | 1830 |
| `_check_managers` | `(**kwargs)` | <p>Perform all manager checks.</p> | python3.13/site-packages/django/db/models/base.py | 1812 |
| `_check_model` | `()` |  | python3.13/site-packages/django/db/models/base.py | 1799 |
| `_check_model_name_db_lookup_clashes` | `()` |  | python3.13/site-packages/django/db/models/base.py | 1980 |
| `_check_ordering` | `()` | <p>Check "ordering" option -- is it a list of strings and do all fields<br>exist?</p> | python3.13/site-packages/django/db/models/base.py | 2215 |
| `_check_property_name_related_field_accessor_clashes` | `()` |  | python3.13/site-packages/django/db/models/base.py | 2004 |
| `_check_single_primary_key` | `()` |  | python3.13/site-packages/django/db/models/base.py | 2025 |
| `_check_swappable` | `()` | <p>Check if the swapped model exists.</p> | python3.13/site-packages/django/db/models/base.py | 1772 |
| `_check_unique_together` | `()` | <p>Check the value of "unique\_together" option.</p> | python3.13/site-packages/django/db/models/base.py | 2039 |
| `_do_insert` | `(self, manager, using, fields, returning_fields, raw)` | <p>Do an INSERT. If returning\_fields is defined then this method should<br>return the newly created data for the model.</p> | python3.13/site-packages/django/db/models/base.py | 1196 |
| `_do_update` | `(self, base_qs, using, pk_val, values, update_fields, forced_update)` | <p>Try to update the model. Return True if the model was updated (if an<br>update query was done and a matching row was found in the DB).</p> | python3.13/site-packages/django/db/models/base.py | 1168 |
| `_get_FIELD_display` | `(self, field)` |  | python3.13/site-packages/django/db/models/base.py | 1284 |
| `_get_expr_references` | `(expr)` |  | python3.13/site-packages/django/db/models/base.py | 2404 |
| `_get_field_expression_map` | `(self, meta, exclude=None)` |  | python3.13/site-packages/django/db/models/base.py | 1336 |
| `_get_next_or_previous_by_FIELD` | `(self, field, is_next, **kwargs)` |  | python3.13/site-packages/django/db/models/base.py | 1292 |
| `_get_next_or_previous_in_order` | `(self, is_next)` |  | python3.13/site-packages/django/db/models/base.py | 1313 |
| `_get_pk_val` | `(self, meta=None)` |  | python3.13/site-packages/django/db/models/base.py | 653 |
| `_get_unique_checks` | `(self, exclude=None, include_meta_constraints=False)` | <p>Return a list of checks to perform. Since validate\_unique() could be<br>called from a ModelForm, some fields may have been excluded; we can't<br>perform a unique check on a model that is missing fields involved<br>in that check. Fields that did not validate should also be excluded,<br>but they need to be passed in via the exclude argument.</p> | python3.13/site-packages/django/db/models/base.py | 1386 |
| `_parse_params` | `(self, *args, method_name, **kwargs)` |  | python3.13/site-packages/django/db/models/base.py | 780 |
| `_perform_date_checks` | `(self, date_checks)` |  | python3.13/site-packages/django/db/models/base.py | 1498 |
| `_perform_unique_checks` | `(self, unique_checks)` |  | python3.13/site-packages/django/db/models/base.py | 1449 |
| `_prepare_related_fields_for_save` | `(self, operation_name, fields=None)` |  | python3.13/site-packages/django/db/models/base.py | 1209 |
| `_save_parents` | `(self, cls, using, update_fields, force_insert, updated_parents=None)` | <p>Save all the parents of cls using values from self.</p> | python3.13/site-packages/django/db/models/base.py | 1023 |
| `_save_table` | `(self, raw=False, cls=None, force_insert=False, force_update=False, using=None, update_fields=None)` | <p>Do the heavy-lifting involved in saving. Update or insert the data<br>for a single table.</p> | python3.13/site-packages/django/db/models/base.py | 1070 |
| `_set_pk_val` | `(self, value)` |  | python3.13/site-packages/django/db/models/base.py | 657 |
| `_validate_force_insert` | `(force_insert)` |  | python3.13/site-packages/django/db/models/base.py | 931 |
| `adelete` | `(self, using=None, keep_parents=False)` |  | python3.13/site-packages/django/db/models/base.py | 1276 |
| `arefresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |  | python3.13/site-packages/django/db/models/base.py | 757 |
| `asave` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |  | python3.13/site-packages/django/db/models/base.py | 904 |
| `check` | `(**kwargs)` |  | python3.13/site-packages/django/db/models/base.py | 1680 |
| `clean` | `(self)` | <p>Hook for doing any extra model-wide validation after clean() has been<br>called on every field by self.clean\_fields. Any ValidationError raised<br>by this method will not be associated with a particular field; it will<br>have a special-case association with the field defined by NON\_FIELD\_ERRORS.</p> | python3.13/site-packages/django/db/models/base.py | 1361 |
| `clean_fields` | `(self, exclude=None)` | <p>Clean all fields and raise a ValidationError containing a dict<br>of all validation errors if any occur.</p> | python3.13/site-packages/django/db/models/base.py | 1652 |
| `date_error_message` | `(self, lookup_type, field_name, unique_for)` |  | python3.13/site-packages/django/db/models/base.py | 1529 |
| `delete` | `(self, using=None, keep_parents=False)` |  | python3.13/site-packages/django/db/models/base.py | 1263 |
| `from_db` | `(db, field_names, values)` |  | python3.13/site-packages/django/db/models/base.py | 574 |
| `full_clean` | `(self, exclude=None, validate_unique=True, validate_constraints=True)` | <p>Call clean\_fields(), clean(), validate\_unique(), and<br>validate\_constraints() on the model. Raise a ValidationError for any<br>errors that occur.</p> | python3.13/site-packages/django/db/models/base.py | 1605 |
| `get_constraints` | `(self)` |  | python3.13/site-packages/django/db/models/base.py | 1578 |
| `get_deferred_fields` | `(self)` | <p>Return a set containing names of deferred fields for this instance.</p> | python3.13/site-packages/django/db/models/base.py | 665 |
| `prepare_database_save` | `(self, field)` |  | python3.13/site-packages/django/db/models/base.py | 1354 |
| `refresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` | <p>Reload field values from the database.</p><p>By default, the reloading happens from the database this instance was<br>loaded from, or by the read router if this instance wasn't loaded from<br>any database. The using parameter will override the default.</p><p>Fields can be used to specify which fields to reload. The fields<br>should be an iterable of field attnames. If fields is None, then<br>all non-deferred fields are reloaded.</p><p>When accessing deferred fields of an instance, the deferred loading<br>of the field will call this method.</p> | python3.13/site-packages/django/db/models/base.py | 675 |
| `save` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` | <p>Save the current instance. Override this in a subclass if you want to<br>control the saving process.</p><p>The 'force\_insert' and 'force\_update' parameters can be used to insist<br>that the "save" must be an SQL insert or update (or equivalent for<br>non-SQL backends), respectively. Normally, they should not be set.</p> | python3.13/site-packages/django/db/models/base.py | 820 |
| `save_base` | `(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None)` | <p>Handle the parts of saving which should be done only once per save,<br>yet need to be done in raw saves, too. This includes some sanity<br>checks and signal sending.</p><p>The 'raw' argument is telling save\_base not to save any parent<br>models and not to do any changes to the values before save. This<br>is used by fixture loading.</p> | python3.13/site-packages/django/db/models/base.py | 951 |
| `serializable_value` | `(self, field_name)` | <p>Return the value of the field name for this instance. If the field is<br>a foreign key, return the id value instead of the object. If there's<br>no Field object with this name on the model, return the model<br>attribute's value.</p><p>Used to serialize a field's value (in the serializer, or form output,<br>for example). Normally, you would just access the attribute directly<br>and not use this method.</p> | python3.13/site-packages/django/db/models/base.py | 762 |
| `unique_error_message` | `(self, model_class, unique_check)` |  | python3.13/site-packages/django/db/models/base.py | 1546 |
| `validate_constraints` | `(self, exclude=None)` |  | python3.13/site-packages/django/db/models/base.py | 1585 |
| `validate_unique` | `(self, exclude=None)` | <p>Check unique constraints on the model and raise ValidationError if any<br>failed.</p> | python3.13/site-packages/django/db/models/base.py | 1370 |


---
