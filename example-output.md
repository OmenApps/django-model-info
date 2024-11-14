# admin.LogEntry

## Model Info

| Key | Value |
|-----|-------|
| Model Name | LogEntry |
| Verbose Name | log entry |
| Verbose Name Plural | log entries |
| Docstring | <p>LogEntry(id, action\_time, user, content\_type, object\_id, object\_repr, action\_flag, change\_message)</p> |
| Is Abstract | False |
| Is Proxy | False |
| Is Managed | True |
| Ordering | ['-action_time'] |
| Permissions | [] |
| Default Permissions | ('add', 'change', 'delete', 'view') |
| Indexes | [] |
| Constraints | [] |
| Database Table | django_admin_log |
| Base Manager | None |
| Default Manager | None |
| File | /home/watervize/github_jacklinke/django-model-info/.venv/lib/python3.11/site-packages/django/contrib/admin/models.py |
| Starting Line Number | 104 |
| Method Resolution Order | (<class 'django.contrib.admin.models.LogEntry'>, <class 'django.db.models.base.Model'>, <class 'django.db.models.utils.AltersData'>, <class 'object'>) |


## Fields

| Field Name | Field Type | Database Column | Database Type | Verbose Name |
|------------|------------|----------------|---------------|--------------|
| `action_flag` | PositiveSmallIntegerField | action_flag | smallint unsigned | action flag |
| `action_time` | DateTimeField | action_time | datetime | action time |
| `change_message` | TextField | change_message | text | change message |
| `content_type` | ForeignKey | content_type_id | integer | content type |
| `id (pk)` | AutoField | id | integer | ID |
| `object_id` | TextField | object_id | text | object id |
| `object_repr` | CharField | object_repr | varchar(200) | object repr |
| `user` | ForeignKey | user_id | integer | user |


## Relations

| Field Name | Field Type | Database Column | Database Type | Related Model | Related Name |
|------------|------------|----------------|---------------|---------------|--------------|
| `content_type` | ForeignKey | content_type_id | integer | contenttypes.ContentType | logentry_set |
| `user` | ForeignKey | user_id | integer | auth.User | logentry_set |


## Methods

### Dunder Methods

| Method Name |Signature |
|-------------|----------|
| `__class__` | `(name, bases, attrs, **kwargs)` |
| `__delattr__` | `(self, name, /)` |
| `__dir__` | `(self, /)` |
| `__eq__` | `(self, other)` |
| `__format__` | `(self, format_spec, /)` |
| `__ge__` | `(self, value, /)` |
| `__getattribute__` | `(self, name, /)` |
| `__getstate__` | `(self)` |
| `__gt__` | `(self, value, /)` |
| `__hash__` | `(self)` |
| `__init__` | `(self, *args, **kwargs)` |
| `__init_subclass__` | `(**kwargs)` |
| `__le__` | `(self, value, /)` |
| `__lt__` | `(self, value, /)` |
| `__ne__` | `(self, value, /)` |
| `__new__` | `(*args, **kwargs)` |
| `__reduce__` | `(self)` |
| `__reduce_ex__` | `(self, protocol, /)` |
| `__repr__` | `(self)` |
| `__setattr__` | `(self, name, value, /)` |
| `__setstate__` | `(self, state)` |
| `__sizeof__` | `(self, /)` |
| `__str__` | `(self)` |
| `__subclasshook__` | `No signature found` |


### Common Django Methods

| Method Name |Signature |
|-------------|----------|
| `_check_column_name_clashes` | `()` |
| `_check_constraints` | `(databases)` |
| `_check_db_table_comment` | `(databases)` |
| `_check_default_pk` | `()` |
| `_check_field_name_clashes` | `()` |
| `_check_fields` | `(**kwargs)` |
| `_check_id_field` | `()` |
| `_check_indexes` | `(databases)` |
| `_check_local_fields` | `(fields, option)` |
| `_check_long_column_names` | `(databases)` |
| `_check_m2m_through_same_relationship` | `()` |
| `_check_managers` | `(**kwargs)` |
| `_check_model` | `()` |
| `_check_model_name_db_lookup_clashes` | `()` |
| `_check_ordering` | `()` |
| `_check_property_name_related_field_accessor_clashes` | `()` |
| `_check_single_primary_key` | `()` |
| `_check_swappable` | `()` |
| `_check_unique_together` | `()` |
| `_do_insert` | `(self, manager, using, fields, returning_fields, raw)` |
| `_do_update` | `(self, base_qs, using, pk_val, values, update_fields, forced_update)` |
| `_get_FIELD_display` | `(self, field)` |
| `_get_expr_references` | `(expr)` |
| `_get_field_expression_map` | `(self, meta, exclude=None)` |
| `_get_next_or_previous_by_FIELD` | `(self, field, is_next, **kwargs)` |
| `_get_next_or_previous_in_order` | `(self, is_next)` |
| `_get_pk_val` | `(self, meta=None)` |
| `_get_unique_checks` | `(self, exclude=None, include_meta_constraints=False)` |
| `_parse_params` | `(self, *args, method_name, **kwargs)` |
| `_perform_date_checks` | `(self, date_checks)` |
| `_perform_unique_checks` | `(self, unique_checks)` |
| `_prepare_related_fields_for_save` | `(self, operation_name, fields=None)` |
| `_save_parents` | `(self, cls, using, update_fields, force_insert, updated_parents=None)` |
| `_save_table` | `(self, raw=False, cls=None, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `_set_pk_val` | `(self, value)` |
| `_validate_force_insert` | `(force_insert)` |
| `adelete` | `(self, using=None, keep_parents=False)` |
| `arefresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `asave` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `check` | `(**kwargs)` |
| `clean` | `(self)` |
| `clean_fields` | `(self, exclude=None)` |
| `date_error_message` | `(self, lookup_type, field_name, unique_for)` |
| `delete` | `(self, using=None, keep_parents=False)` |
| `from_db` | `(db, field_names, values)` |
| `full_clean` | `(self, exclude=None, validate_unique=True, validate_constraints=True)` |
| `get_constraints` | `(self)` |
| `get_deferred_fields` | `(self)` |
| `prepare_database_save` | `(self, field)` |
| `refresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `save` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `save_base` | `(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `serializable_value` | `(self, field_name)` |
| `unique_error_message` | `(self, model_class, unique_check)` |
| `validate_constraints` | `(self, exclude=None)` |
| `validate_unique` | `(self, exclude=None)` |


### Other Methods

| Method Name |Signature |
|-------------|----------|
| `get_action_flag_display` | `(self, *, field=<django.db.models.fields.PositiveSmallIntegerField: action_flag>)` |
| `get_admin_url` | `(self)` |
| `get_change_message` | `(self)` |
| `get_edited_object` | `(self)` |
| `get_next_by_action_time` | `(self, *, field=<django.db.models.fields.DateTimeField: action_time>, is_next=True, **kwargs)` |
| `get_previous_by_action_time` | `(self, *, field=<django.db.models.fields.DateTimeField: action_time>, is_next=False, **kwargs)` |
| `is_addition` | `(self)` |
| `is_change` | `(self)` |
| `is_deletion` | `(self)` |


---

# auth.Group

## Model Info

| Key | Value |
|-----|-------|
| Model Name | Group |
| Verbose Name | group |
| Verbose Name Plural | groups |
| Docstring | <p>Groups are a generic way of categorizing users to apply permissions, or<br>some other label, to those users. A user can belong to any number of<br>groups.</p><p>A user in a group automatically has all the permissions granted to that<br>group. For example, if the group 'Site editors' has the permission<br>can\_edit\_home\_page, any user in that group will have that permission.</p><p>Beyond permissions, groups are a convenient way to categorize users to<br>apply some label, or extended functionality, to them. For example, you<br>could create a group 'Special users', and you could write code that would<br>do special things to those users -- such as giving them access to a<br>members-only portion of your site, or sending them members-only email<br>messages.</p> |
| Is Abstract | False |
| Is Proxy | False |
| Is Managed | True |
| Ordering | [] |
| Permissions | [] |
| Default Permissions | ('add', 'change', 'delete', 'view') |
| Indexes | [] |
| Constraints | [] |
| Database Table | auth_group |
| Base Manager | None |
| Default Manager | None |
| File | /home/watervize/github_jacklinke/django-model-info/.venv/lib/python3.11/site-packages/django/contrib/auth/models.py |
| Starting Line Number | 99 |
| Method Resolution Order | (<class 'django.contrib.auth.models.Group'>, <class 'django.db.models.base.Model'>, <class 'django.db.models.utils.AltersData'>, <class 'object'>) |


## Fields

| Field Name | Field Type | Database Column | Database Type | Verbose Name |
|------------|------------|----------------|---------------|--------------|
| `Group_permissions+` | ManyToOneRel |  | integer |  |
| `User_groups+` | ManyToOneRel |  | integer |  |
| `id (pk)` | AutoField | id | integer | ID |
| `name` | CharField | name | varchar(150) | name |
| `permissions` | ManyToManyField | permissions | through auth.Group_permissions | permissions |
| `user` | ManyToManyRel |  | through auth.User_groups |  |


## Relations

| Field Name | Field Type | Database Column | Database Type | Related Model | Related Name |
|------------|------------|----------------|---------------|---------------|--------------|
| `permissions` | ManyToManyField | permissions | through auth.Group_permissions | auth.Permission | group_set |


## Methods

### Dunder Methods

| Method Name |Signature |
|-------------|----------|
| `__class__` | `(name, bases, attrs, **kwargs)` |
| `__delattr__` | `(self, name, /)` |
| `__dir__` | `(self, /)` |
| `__eq__` | `(self, other)` |
| `__format__` | `(self, format_spec, /)` |
| `__ge__` | `(self, value, /)` |
| `__getattribute__` | `(self, name, /)` |
| `__getstate__` | `(self)` |
| `__gt__` | `(self, value, /)` |
| `__hash__` | `(self)` |
| `__init__` | `(self, *args, **kwargs)` |
| `__init_subclass__` | `(**kwargs)` |
| `__le__` | `(self, value, /)` |
| `__lt__` | `(self, value, /)` |
| `__ne__` | `(self, value, /)` |
| `__new__` | `(*args, **kwargs)` |
| `__reduce__` | `(self)` |
| `__reduce_ex__` | `(self, protocol, /)` |
| `__repr__` | `(self)` |
| `__setattr__` | `(self, name, value, /)` |
| `__setstate__` | `(self, state)` |
| `__sizeof__` | `(self, /)` |
| `__str__` | `(self)` |
| `__subclasshook__` | `No signature found` |


### Common Django Methods

| Method Name |Signature |
|-------------|----------|
| `_check_column_name_clashes` | `()` |
| `_check_constraints` | `(databases)` |
| `_check_db_table_comment` | `(databases)` |
| `_check_default_pk` | `()` |
| `_check_field_name_clashes` | `()` |
| `_check_fields` | `(**kwargs)` |
| `_check_id_field` | `()` |
| `_check_indexes` | `(databases)` |
| `_check_local_fields` | `(fields, option)` |
| `_check_long_column_names` | `(databases)` |
| `_check_m2m_through_same_relationship` | `()` |
| `_check_managers` | `(**kwargs)` |
| `_check_model` | `()` |
| `_check_model_name_db_lookup_clashes` | `()` |
| `_check_ordering` | `()` |
| `_check_property_name_related_field_accessor_clashes` | `()` |
| `_check_single_primary_key` | `()` |
| `_check_swappable` | `()` |
| `_check_unique_together` | `()` |
| `_do_insert` | `(self, manager, using, fields, returning_fields, raw)` |
| `_do_update` | `(self, base_qs, using, pk_val, values, update_fields, forced_update)` |
| `_get_FIELD_display` | `(self, field)` |
| `_get_expr_references` | `(expr)` |
| `_get_field_expression_map` | `(self, meta, exclude=None)` |
| `_get_next_or_previous_by_FIELD` | `(self, field, is_next, **kwargs)` |
| `_get_next_or_previous_in_order` | `(self, is_next)` |
| `_get_pk_val` | `(self, meta=None)` |
| `_get_unique_checks` | `(self, exclude=None, include_meta_constraints=False)` |
| `_parse_params` | `(self, *args, method_name, **kwargs)` |
| `_perform_date_checks` | `(self, date_checks)` |
| `_perform_unique_checks` | `(self, unique_checks)` |
| `_prepare_related_fields_for_save` | `(self, operation_name, fields=None)` |
| `_save_parents` | `(self, cls, using, update_fields, force_insert, updated_parents=None)` |
| `_save_table` | `(self, raw=False, cls=None, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `_set_pk_val` | `(self, value)` |
| `_validate_force_insert` | `(force_insert)` |
| `adelete` | `(self, using=None, keep_parents=False)` |
| `arefresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `asave` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `check` | `(**kwargs)` |
| `clean` | `(self)` |
| `clean_fields` | `(self, exclude=None)` |
| `date_error_message` | `(self, lookup_type, field_name, unique_for)` |
| `delete` | `(self, using=None, keep_parents=False)` |
| `from_db` | `(db, field_names, values)` |
| `full_clean` | `(self, exclude=None, validate_unique=True, validate_constraints=True)` |
| `get_constraints` | `(self)` |
| `get_deferred_fields` | `(self)` |
| `prepare_database_save` | `(self, field)` |
| `refresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `save` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `save_base` | `(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `serializable_value` | `(self, field_name)` |
| `unique_error_message` | `(self, model_class, unique_check)` |
| `validate_constraints` | `(self, exclude=None)` |
| `validate_unique` | `(self, exclude=None)` |


### Other Methods

| Method Name |Signature |
|-------------|----------|
| `natural_key` | `(self)` |


---

# auth.Permission

## Model Info

| Key | Value |
|-----|-------|
| Model Name | Permission |
| Verbose Name | permission |
| Verbose Name Plural | permissions |
| Docstring | <p>The permissions system provides a way to assign permissions to specific<br>users and groups of users.</p><p>The permission system is used by the Django admin site, but may also be<br>useful in your own code. The Django admin site uses permissions as follows:</p><p>    - The "add" permission limits the user's ability to view the "add" form<br>      and add an object.<br>    - The "change" permission limits a user's ability to view the change<br>      list, view the "change" form and change an object.<br>    - The "delete" permission limits the ability to delete an object.<br>    - The "view" permission limits the ability to view an object.</p><p>Permissions are set globally per type of object, not per specific object<br>instance. It is possible to say "Mary may change news stories," but it's<br>not currently possible to say "Mary may change news stories, but only the<br>ones she created herself" or "Mary may only change news stories that have a<br>certain status or publication date."</p><p>The permissions listed above are automatically created for each model.</p> |
| Is Abstract | False |
| Is Proxy | False |
| Is Managed | True |
| Ordering | ['content_type__app_label', 'content_type__model', 'codename'] |
| Permissions | [] |
| Default Permissions | ('add', 'change', 'delete', 'view') |
| Indexes | [] |
| Constraints | [] |
| Database Table | auth_permission |
| Base Manager | None |
| Default Manager | None |
| File | /home/watervize/github_jacklinke/django-model-info/.venv/lib/python3.11/site-packages/django/contrib/auth/models.py |
| Starting Line Number | 39 |
| Method Resolution Order | (<class 'django.contrib.auth.models.Permission'>, <class 'django.db.models.base.Model'>, <class 'django.db.models.utils.AltersData'>, <class 'object'>) |


## Fields

| Field Name | Field Type | Database Column | Database Type | Verbose Name |
|------------|------------|----------------|---------------|--------------|
| `Group_permissions+` | ManyToOneRel |  | integer |  |
| `User_user_permissions+` | ManyToOneRel |  | integer |  |
| `codename` | CharField | codename | varchar(100) | codename |
| `content_type` | ForeignKey | content_type_id | integer | content type |
| `group` | ManyToManyRel |  | through auth.Group_permissions |  |
| `id (pk)` | AutoField | id | integer | ID |
| `name` | CharField | name | varchar(255) | name |
| `user` | ManyToManyRel |  | through auth.User_user_permissions |  |


## Relations

| Field Name | Field Type | Database Column | Database Type | Related Model | Related Name |
|------------|------------|----------------|---------------|---------------|--------------|
| `content_type` | ForeignKey | content_type_id | integer | contenttypes.ContentType | permission_set |


## Methods

### Dunder Methods

| Method Name |Signature |
|-------------|----------|
| `__class__` | `(name, bases, attrs, **kwargs)` |
| `__delattr__` | `(self, name, /)` |
| `__dir__` | `(self, /)` |
| `__eq__` | `(self, other)` |
| `__format__` | `(self, format_spec, /)` |
| `__ge__` | `(self, value, /)` |
| `__getattribute__` | `(self, name, /)` |
| `__getstate__` | `(self)` |
| `__gt__` | `(self, value, /)` |
| `__hash__` | `(self)` |
| `__init__` | `(self, *args, **kwargs)` |
| `__init_subclass__` | `(**kwargs)` |
| `__le__` | `(self, value, /)` |
| `__lt__` | `(self, value, /)` |
| `__ne__` | `(self, value, /)` |
| `__new__` | `(*args, **kwargs)` |
| `__reduce__` | `(self)` |
| `__reduce_ex__` | `(self, protocol, /)` |
| `__repr__` | `(self)` |
| `__setattr__` | `(self, name, value, /)` |
| `__setstate__` | `(self, state)` |
| `__sizeof__` | `(self, /)` |
| `__str__` | `(self)` |
| `__subclasshook__` | `No signature found` |


### Common Django Methods

| Method Name |Signature |
|-------------|----------|
| `_check_column_name_clashes` | `()` |
| `_check_constraints` | `(databases)` |
| `_check_db_table_comment` | `(databases)` |
| `_check_default_pk` | `()` |
| `_check_field_name_clashes` | `()` |
| `_check_fields` | `(**kwargs)` |
| `_check_id_field` | `()` |
| `_check_indexes` | `(databases)` |
| `_check_local_fields` | `(fields, option)` |
| `_check_long_column_names` | `(databases)` |
| `_check_m2m_through_same_relationship` | `()` |
| `_check_managers` | `(**kwargs)` |
| `_check_model` | `()` |
| `_check_model_name_db_lookup_clashes` | `()` |
| `_check_ordering` | `()` |
| `_check_property_name_related_field_accessor_clashes` | `()` |
| `_check_single_primary_key` | `()` |
| `_check_swappable` | `()` |
| `_check_unique_together` | `()` |
| `_do_insert` | `(self, manager, using, fields, returning_fields, raw)` |
| `_do_update` | `(self, base_qs, using, pk_val, values, update_fields, forced_update)` |
| `_get_FIELD_display` | `(self, field)` |
| `_get_expr_references` | `(expr)` |
| `_get_field_expression_map` | `(self, meta, exclude=None)` |
| `_get_next_or_previous_by_FIELD` | `(self, field, is_next, **kwargs)` |
| `_get_next_or_previous_in_order` | `(self, is_next)` |
| `_get_pk_val` | `(self, meta=None)` |
| `_get_unique_checks` | `(self, exclude=None, include_meta_constraints=False)` |
| `_parse_params` | `(self, *args, method_name, **kwargs)` |
| `_perform_date_checks` | `(self, date_checks)` |
| `_perform_unique_checks` | `(self, unique_checks)` |
| `_prepare_related_fields_for_save` | `(self, operation_name, fields=None)` |
| `_save_parents` | `(self, cls, using, update_fields, force_insert, updated_parents=None)` |
| `_save_table` | `(self, raw=False, cls=None, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `_set_pk_val` | `(self, value)` |
| `_validate_force_insert` | `(force_insert)` |
| `adelete` | `(self, using=None, keep_parents=False)` |
| `arefresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `asave` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `check` | `(**kwargs)` |
| `clean` | `(self)` |
| `clean_fields` | `(self, exclude=None)` |
| `date_error_message` | `(self, lookup_type, field_name, unique_for)` |
| `delete` | `(self, using=None, keep_parents=False)` |
| `from_db` | `(db, field_names, values)` |
| `full_clean` | `(self, exclude=None, validate_unique=True, validate_constraints=True)` |
| `get_constraints` | `(self)` |
| `get_deferred_fields` | `(self)` |
| `prepare_database_save` | `(self, field)` |
| `refresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `save` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `save_base` | `(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `serializable_value` | `(self, field_name)` |
| `unique_error_message` | `(self, model_class, unique_check)` |
| `validate_constraints` | `(self, exclude=None)` |
| `validate_unique` | `(self, exclude=None)` |


### Other Methods

| Method Name |Signature |
|-------------|----------|
| `natural_key` | `(self)` |


---

# auth.User

## Model Info

| Key | Value |
|-----|-------|
| Model Name | User |
| Verbose Name | user |
| Verbose Name Plural | users |
| Docstring | <p>Users within the Django authentication system are represented by this<br>model.</p><p>Username and password are required. Other fields are optional.</p> |
| Is Abstract | False |
| Is Proxy | False |
| Is Managed | True |
| Ordering | [] |
| Permissions | [] |
| Default Permissions | ('add', 'change', 'delete', 'view') |
| Indexes | [] |
| Constraints | [] |
| Database Table | auth_user |
| Base Manager | None |
| Default Manager | None |
| File | /home/watervize/github_jacklinke/django-model-info/.venv/lib/python3.11/site-packages/django/contrib/auth/models.py |
| Starting Line Number | 406 |
| Method Resolution Order | (<class 'django.contrib.auth.models.User'>, <class 'django.contrib.auth.models.AbstractUser'>, <class 'django.contrib.auth.base_user.AbstractBaseUser'>, <class 'django.contrib.auth.models.PermissionsMixin'>, <class 'django.db.models.base.Model'>, <class 'django.db.models.utils.AltersData'>, <class 'object'>) |


## Fields

| Field Name | Field Type | Database Column | Database Type | Verbose Name |
|------------|------------|----------------|---------------|--------------|
| `User_groups+` | ManyToOneRel |  | integer |  |
| `User_user_permissions+` | ManyToOneRel |  | integer |  |
| `date_joined` | DateTimeField | date_joined | datetime | date joined |
| `email` | EmailField | email | varchar(254) | email address |
| `first_name` | CharField | first_name | varchar(150) | first name |
| `groups` | ManyToManyField | groups | through auth.User_groups | groups |
| `id (pk)` | AutoField | id | integer | ID |
| `is_active` | BooleanField | is_active | bool | active |
| `is_staff` | BooleanField | is_staff | bool | staff status |
| `is_superuser` | BooleanField | is_superuser | bool | superuser status |
| `last_login` | DateTimeField | last_login | datetime | last login |
| `last_name` | CharField | last_name | varchar(150) | last name |
| `logentry` | ManyToOneRel |  | integer |  |
| `password` | CharField | password | varchar(128) | password |
| `profile` | OneToOneRel |  | integer |  |
| `user_permissions` | ManyToManyField | user_permissions | through auth.User_user_permissions | user permissions |
| `username` | CharField | username | varchar(150) | username |


## Relations

| Field Name | Field Type | Database Column | Database Type | Related Model | Related Name |
|------------|------------|----------------|---------------|---------------|--------------|
| `groups` | ManyToManyField | groups | through auth.User_groups | auth.Group | user_set |
| `user_permissions` | ManyToManyField | user_permissions | through auth.User_user_permissions | auth.Permission | user_set |


## Methods

### Dunder Methods

| Method Name |Signature |
|-------------|----------|
| `__class__` | `(name, bases, attrs, **kwargs)` |
| `__delattr__` | `(self, name, /)` |
| `__dir__` | `(self, /)` |
| `__eq__` | `(self, other)` |
| `__format__` | `(self, format_spec, /)` |
| `__ge__` | `(self, value, /)` |
| `__getattribute__` | `(self, name, /)` |
| `__getstate__` | `(self)` |
| `__gt__` | `(self, value, /)` |
| `__hash__` | `(self)` |
| `__init__` | `(self, *args, **kwargs)` |
| `__init_subclass__` | `(**kwargs)` |
| `__le__` | `(self, value, /)` |
| `__lt__` | `(self, value, /)` |
| `__ne__` | `(self, value, /)` |
| `__new__` | `(*args, **kwargs)` |
| `__reduce__` | `(self)` |
| `__reduce_ex__` | `(self, protocol, /)` |
| `__repr__` | `(self)` |
| `__setattr__` | `(self, name, value, /)` |
| `__setstate__` | `(self, state)` |
| `__sizeof__` | `(self, /)` |
| `__str__` | `(self)` |
| `__subclasshook__` | `No signature found` |


### Common Django Methods

| Method Name |Signature |
|-------------|----------|
| `_check_column_name_clashes` | `()` |
| `_check_constraints` | `(databases)` |
| `_check_db_table_comment` | `(databases)` |
| `_check_default_pk` | `()` |
| `_check_field_name_clashes` | `()` |
| `_check_fields` | `(**kwargs)` |
| `_check_id_field` | `()` |
| `_check_indexes` | `(databases)` |
| `_check_local_fields` | `(fields, option)` |
| `_check_long_column_names` | `(databases)` |
| `_check_m2m_through_same_relationship` | `()` |
| `_check_managers` | `(**kwargs)` |
| `_check_model` | `()` |
| `_check_model_name_db_lookup_clashes` | `()` |
| `_check_ordering` | `()` |
| `_check_property_name_related_field_accessor_clashes` | `()` |
| `_check_single_primary_key` | `()` |
| `_check_swappable` | `()` |
| `_check_unique_together` | `()` |
| `_do_insert` | `(self, manager, using, fields, returning_fields, raw)` |
| `_do_update` | `(self, base_qs, using, pk_val, values, update_fields, forced_update)` |
| `_get_FIELD_display` | `(self, field)` |
| `_get_expr_references` | `(expr)` |
| `_get_field_expression_map` | `(self, meta, exclude=None)` |
| `_get_next_or_previous_by_FIELD` | `(self, field, is_next, **kwargs)` |
| `_get_next_or_previous_in_order` | `(self, is_next)` |
| `_get_pk_val` | `(self, meta=None)` |
| `_get_unique_checks` | `(self, exclude=None, include_meta_constraints=False)` |
| `_parse_params` | `(self, *args, method_name, **kwargs)` |
| `_perform_date_checks` | `(self, date_checks)` |
| `_perform_unique_checks` | `(self, unique_checks)` |
| `_prepare_related_fields_for_save` | `(self, operation_name, fields=None)` |
| `_save_parents` | `(self, cls, using, update_fields, force_insert, updated_parents=None)` |
| `_save_table` | `(self, raw=False, cls=None, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `_set_pk_val` | `(self, value)` |
| `_validate_force_insert` | `(force_insert)` |
| `adelete` | `(self, using=None, keep_parents=False)` |
| `arefresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `asave` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `check` | `(**kwargs)` |
| `clean` | `(self)` |
| `clean_fields` | `(self, exclude=None)` |
| `date_error_message` | `(self, lookup_type, field_name, unique_for)` |
| `delete` | `(self, using=None, keep_parents=False)` |
| `from_db` | `(db, field_names, values)` |
| `full_clean` | `(self, exclude=None, validate_unique=True, validate_constraints=True)` |
| `get_constraints` | `(self)` |
| `get_deferred_fields` | `(self)` |
| `prepare_database_save` | `(self, field)` |
| `refresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `save` | `(self, *args, **kwargs)` |
| `save_base` | `(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `serializable_value` | `(self, field_name)` |
| `unique_error_message` | `(self, model_class, unique_check)` |
| `validate_constraints` | `(self, exclude=None)` |
| `validate_unique` | `(self, exclude=None)` |


### Private Methods

| Method Name |Signature |
|-------------|----------|
| `_get_session_auth_hash` | `(self, secret=None)` |


### Other Methods

| Method Name |Signature |
|-------------|----------|
| `acheck_password` | `(self, raw_password)` |
| `check_password` | `(self, raw_password)` |
| `email_user` | `(self, subject, message, from_email=None, **kwargs)` |
| `get_all_permissions` | `(self, obj=None)` |
| `get_email_field_name` | `()` |
| `get_full_name` | `(self)` |
| `get_group_permissions` | `(self, obj=None)` |
| `get_next_by_date_joined` | `(self, *, field=<django.db.models.fields.DateTimeField: date_joined>, is_next=True, **kwargs)` |
| `get_previous_by_date_joined` | `(self, *, field=<django.db.models.fields.DateTimeField: date_joined>, is_next=False, **kwargs)` |
| `get_session_auth_fallback_hash` | `(self)` |
| `get_session_auth_hash` | `(self)` |
| `get_short_name` | `(self)` |
| `get_user_permissions` | `(self, obj=None)` |
| `get_username` | `(self)` |
| `has_module_perms` | `(self, app_label)` |
| `has_perm` | `(self, perm, obj=None)` |
| `has_perms` | `(self, perm_list, obj=None)` |
| `has_usable_password` | `(self)` |
| `natural_key` | `(self)` |
| `normalize_username` | `(username)` |
| `set_password` | `(self, raw_password)` |
| `set_unusable_password` | `(self)` |
| `username_validator` | `(value)` |


---

# contenttypes.ContentType

## Model Info

| Key | Value |
|-----|-------|
| Model Name | ContentType |
| Verbose Name | content type |
| Verbose Name Plural | content types |
| Docstring | <p>ContentType(id, app\_label, model)</p> |
| Is Abstract | False |
| Is Proxy | False |
| Is Managed | True |
| Ordering | [] |
| Permissions | [] |
| Default Permissions | ('add', 'change', 'delete', 'view') |
| Indexes | [] |
| Constraints | [] |
| Database Table | django_content_type |
| Base Manager | None |
| Default Manager | None |
| File | /home/watervize/github_jacklinke/django-model-info/.venv/lib/python3.11/site-packages/django/contrib/contenttypes/models.py |
| Starting Line Number | 134 |
| Method Resolution Order | (<class 'django.contrib.contenttypes.models.ContentType'>, <class 'django.db.models.base.Model'>, <class 'django.db.models.utils.AltersData'>, <class 'object'>) |


## Fields

| Field Name | Field Type | Database Column | Database Type | Verbose Name |
|------------|------------|----------------|---------------|--------------|
| `app_label` | CharField | app_label | varchar(100) | app label |
| `id (pk)` | AutoField | id | integer | ID |
| `logentry` | ManyToOneRel |  | integer |  |
| `model` | CharField | model | varchar(100) | python model class name |
| `permission` | ManyToOneRel |  | integer |  |


## Methods

### Dunder Methods

| Method Name |Signature |
|-------------|----------|
| `__class__` | `(name, bases, attrs, **kwargs)` |
| `__delattr__` | `(self, name, /)` |
| `__dir__` | `(self, /)` |
| `__eq__` | `(self, other)` |
| `__format__` | `(self, format_spec, /)` |
| `__ge__` | `(self, value, /)` |
| `__getattribute__` | `(self, name, /)` |
| `__getstate__` | `(self)` |
| `__gt__` | `(self, value, /)` |
| `__hash__` | `(self)` |
| `__init__` | `(self, *args, **kwargs)` |
| `__init_subclass__` | `(**kwargs)` |
| `__le__` | `(self, value, /)` |
| `__lt__` | `(self, value, /)` |
| `__ne__` | `(self, value, /)` |
| `__new__` | `(*args, **kwargs)` |
| `__reduce__` | `(self)` |
| `__reduce_ex__` | `(self, protocol, /)` |
| `__repr__` | `(self)` |
| `__setattr__` | `(self, name, value, /)` |
| `__setstate__` | `(self, state)` |
| `__sizeof__` | `(self, /)` |
| `__str__` | `(self)` |
| `__subclasshook__` | `No signature found` |


### Common Django Methods

| Method Name |Signature |
|-------------|----------|
| `_check_column_name_clashes` | `()` |
| `_check_constraints` | `(databases)` |
| `_check_db_table_comment` | `(databases)` |
| `_check_default_pk` | `()` |
| `_check_field_name_clashes` | `()` |
| `_check_fields` | `(**kwargs)` |
| `_check_id_field` | `()` |
| `_check_indexes` | `(databases)` |
| `_check_local_fields` | `(fields, option)` |
| `_check_long_column_names` | `(databases)` |
| `_check_m2m_through_same_relationship` | `()` |
| `_check_managers` | `(**kwargs)` |
| `_check_model` | `()` |
| `_check_model_name_db_lookup_clashes` | `()` |
| `_check_ordering` | `()` |
| `_check_property_name_related_field_accessor_clashes` | `()` |
| `_check_single_primary_key` | `()` |
| `_check_swappable` | `()` |
| `_check_unique_together` | `()` |
| `_do_insert` | `(self, manager, using, fields, returning_fields, raw)` |
| `_do_update` | `(self, base_qs, using, pk_val, values, update_fields, forced_update)` |
| `_get_FIELD_display` | `(self, field)` |
| `_get_expr_references` | `(expr)` |
| `_get_field_expression_map` | `(self, meta, exclude=None)` |
| `_get_next_or_previous_by_FIELD` | `(self, field, is_next, **kwargs)` |
| `_get_next_or_previous_in_order` | `(self, is_next)` |
| `_get_pk_val` | `(self, meta=None)` |
| `_get_unique_checks` | `(self, exclude=None, include_meta_constraints=False)` |
| `_parse_params` | `(self, *args, method_name, **kwargs)` |
| `_perform_date_checks` | `(self, date_checks)` |
| `_perform_unique_checks` | `(self, unique_checks)` |
| `_prepare_related_fields_for_save` | `(self, operation_name, fields=None)` |
| `_save_parents` | `(self, cls, using, update_fields, force_insert, updated_parents=None)` |
| `_save_table` | `(self, raw=False, cls=None, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `_set_pk_val` | `(self, value)` |
| `_validate_force_insert` | `(force_insert)` |
| `adelete` | `(self, using=None, keep_parents=False)` |
| `arefresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `asave` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `check` | `(**kwargs)` |
| `clean` | `(self)` |
| `clean_fields` | `(self, exclude=None)` |
| `date_error_message` | `(self, lookup_type, field_name, unique_for)` |
| `delete` | `(self, using=None, keep_parents=False)` |
| `from_db` | `(db, field_names, values)` |
| `full_clean` | `(self, exclude=None, validate_unique=True, validate_constraints=True)` |
| `get_constraints` | `(self)` |
| `get_deferred_fields` | `(self)` |
| `prepare_database_save` | `(self, field)` |
| `refresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `save` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `save_base` | `(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `serializable_value` | `(self, field_name)` |
| `unique_error_message` | `(self, model_class, unique_check)` |
| `validate_constraints` | `(self, exclude=None)` |
| `validate_unique` | `(self, exclude=None)` |


### Other Methods

| Method Name |Signature |
|-------------|----------|
| `get_all_objects_for_this_type` | `(self, **kwargs)` |
| `get_object_for_this_type` | `(self, using=None, **kwargs)` |
| `model_class` | `(self)` |
| `natural_key` | `(self)` |


---

# example.Author

## Model Info

| Key | Value |
|-----|-------|
| Model Name | Author |
| Verbose Name | author |
| Verbose Name Plural | authors |
| Docstring | <p>Example Author model.</p> |
| Is Abstract | False |
| Is Proxy | False |
| Is Managed | True |
| Ordering | [] |
| Permissions | [] |
| Default Permissions | ('add', 'change', 'delete', 'view') |
| Indexes | [] |
| Constraints | [] |
| Database Table | example_author |
| Base Manager | None |
| Default Manager | None |
| File | /home/watervize/github_jacklinke/django-model-info/tests/example/models.py |
| Starting Line Number | 27 |
| Method Resolution Order | (<class 'tests.example.models.Author'>, <class 'django.db.models.base.Model'>, <class 'django.db.models.utils.AltersData'>, <class 'object'>) |


## Fields

| Field Name | Field Type | Database Column | Database Type | Verbose Name |
|------------|------------|----------------|---------------|--------------|
| `Book_authors+` | ManyToOneRel |  | bigint |  |
| `birth_date` | DateField | birth_date | date | birth date |
| `book` | ManyToManyRel |  | through example.Book_authors |  |
| `first_name` | CharField | first_name | varchar(50) | first name |
| `id (pk)` | BigAutoField | id | integer | ID |
| `last_name` | CharField | last_name | varchar(50) | last name |


## Methods

### Dunder Methods

| Method Name |Signature |
|-------------|----------|
| `__class__` | `(name, bases, attrs, **kwargs)` |
| `__delattr__` | `(self, name, /)` |
| `__dir__` | `(self, /)` |
| `__eq__` | `(self, other)` |
| `__format__` | `(self, format_spec, /)` |
| `__ge__` | `(self, value, /)` |
| `__getattribute__` | `(self, name, /)` |
| `__getstate__` | `(self)` |
| `__gt__` | `(self, value, /)` |
| `__hash__` | `(self)` |
| `__init__` | `(self, *args, **kwargs)` |
| `__init_subclass__` | `(**kwargs)` |
| `__le__` | `(self, value, /)` |
| `__lt__` | `(self, value, /)` |
| `__ne__` | `(self, value, /)` |
| `__new__` | `(*args, **kwargs)` |
| `__reduce__` | `(self)` |
| `__reduce_ex__` | `(self, protocol, /)` |
| `__repr__` | `(self)` |
| `__setattr__` | `(self, name, value, /)` |
| `__setstate__` | `(self, state)` |
| `__sizeof__` | `(self, /)` |
| `__str__` | `(self)` |
| `__subclasshook__` | `No signature found` |


### Common Django Methods

| Method Name |Signature |
|-------------|----------|
| `_check_column_name_clashes` | `()` |
| `_check_constraints` | `(databases)` |
| `_check_db_table_comment` | `(databases)` |
| `_check_default_pk` | `()` |
| `_check_field_name_clashes` | `()` |
| `_check_fields` | `(**kwargs)` |
| `_check_id_field` | `()` |
| `_check_indexes` | `(databases)` |
| `_check_local_fields` | `(fields, option)` |
| `_check_long_column_names` | `(databases)` |
| `_check_m2m_through_same_relationship` | `()` |
| `_check_managers` | `(**kwargs)` |
| `_check_model` | `()` |
| `_check_model_name_db_lookup_clashes` | `()` |
| `_check_ordering` | `()` |
| `_check_property_name_related_field_accessor_clashes` | `()` |
| `_check_single_primary_key` | `()` |
| `_check_swappable` | `()` |
| `_check_unique_together` | `()` |
| `_do_insert` | `(self, manager, using, fields, returning_fields, raw)` |
| `_do_update` | `(self, base_qs, using, pk_val, values, update_fields, forced_update)` |
| `_get_FIELD_display` | `(self, field)` |
| `_get_expr_references` | `(expr)` |
| `_get_field_expression_map` | `(self, meta, exclude=None)` |
| `_get_next_or_previous_by_FIELD` | `(self, field, is_next, **kwargs)` |
| `_get_next_or_previous_in_order` | `(self, is_next)` |
| `_get_pk_val` | `(self, meta=None)` |
| `_get_unique_checks` | `(self, exclude=None, include_meta_constraints=False)` |
| `_parse_params` | `(self, *args, method_name, **kwargs)` |
| `_perform_date_checks` | `(self, date_checks)` |
| `_perform_unique_checks` | `(self, unique_checks)` |
| `_prepare_related_fields_for_save` | `(self, operation_name, fields=None)` |
| `_save_parents` | `(self, cls, using, update_fields, force_insert, updated_parents=None)` |
| `_save_table` | `(self, raw=False, cls=None, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `_set_pk_val` | `(self, value)` |
| `_validate_force_insert` | `(force_insert)` |
| `adelete` | `(self, using=None, keep_parents=False)` |
| `arefresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `asave` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `check` | `(**kwargs)` |
| `clean` | `(self)` |
| `clean_fields` | `(self, exclude=None)` |
| `date_error_message` | `(self, lookup_type, field_name, unique_for)` |
| `delete` | `(self, using=None, keep_parents=False)` |
| `from_db` | `(db, field_names, values)` |
| `full_clean` | `(self, exclude=None, validate_unique=True, validate_constraints=True)` |
| `get_constraints` | `(self)` |
| `get_deferred_fields` | `(self)` |
| `prepare_database_save` | `(self, field)` |
| `refresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `save` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `save_base` | `(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `serializable_value` | `(self, field_name)` |
| `unique_error_message` | `(self, model_class, unique_check)` |
| `validate_constraints` | `(self, exclude=None)` |
| `validate_unique` | `(self, exclude=None)` |


### Other Methods

| Method Name |Signature |
|-------------|----------|
| `get_next_by_birth_date` | `(self, *, field=<django.db.models.fields.DateField: birth_date>, is_next=True, **kwargs)` |
| `get_previous_by_birth_date` | `(self, *, field=<django.db.models.fields.DateField: birth_date>, is_next=False, **kwargs)` |


---

# example.AuthorProxy

## Model Info

| Key | Value |
|-----|-------|
| Model Name | AuthorProxy |
| Verbose Name | author proxy |
| Verbose Name Plural | author proxys |
| Docstring | <p>Example Author proxy model.</p> |
| Is Abstract | False |
| Is Proxy | True |
| Is Managed | True |
| Ordering | ['last_name', 'first_name'] |
| Permissions | [] |
| Default Permissions | ('add', 'change', 'delete', 'view') |
| Indexes | [] |
| Constraints | [] |
| Database Table | example_author |
| Base Manager | None |
| Default Manager | None |
| File | /home/watervize/github_jacklinke/django-model-info/tests/example/models.py |
| Starting Line Number | 45 |
| Method Resolution Order | (<class 'tests.example.models.AuthorProxy'>, <class 'tests.example.models.Author'>, <class 'django.db.models.base.Model'>, <class 'django.db.models.utils.AltersData'>, <class 'object'>) |


## Fields

| Field Name | Field Type | Database Column | Database Type | Verbose Name |
|------------|------------|----------------|---------------|--------------|
| `Book_authors+` | ManyToOneRel |  | bigint |  |
| `birth_date` | DateField | birth_date | date | birth date |
| `book` | ManyToManyRel |  | through example.Book_authors |  |
| `first_name` | CharField | first_name | varchar(50) | first name |
| `id (pk)` | BigAutoField | id | integer | ID |
| `last_name` | CharField | last_name | varchar(50) | last name |


## Methods

### Dunder Methods

| Method Name |Signature |
|-------------|----------|
| `__class__` | `(name, bases, attrs, **kwargs)` |
| `__delattr__` | `(self, name, /)` |
| `__dir__` | `(self, /)` |
| `__eq__` | `(self, other)` |
| `__format__` | `(self, format_spec, /)` |
| `__ge__` | `(self, value, /)` |
| `__getattribute__` | `(self, name, /)` |
| `__getstate__` | `(self)` |
| `__gt__` | `(self, value, /)` |
| `__hash__` | `(self)` |
| `__init__` | `(self, *args, **kwargs)` |
| `__init_subclass__` | `(**kwargs)` |
| `__le__` | `(self, value, /)` |
| `__lt__` | `(self, value, /)` |
| `__ne__` | `(self, value, /)` |
| `__new__` | `(*args, **kwargs)` |
| `__reduce__` | `(self)` |
| `__reduce_ex__` | `(self, protocol, /)` |
| `__repr__` | `(self)` |
| `__setattr__` | `(self, name, value, /)` |
| `__setstate__` | `(self, state)` |
| `__sizeof__` | `(self, /)` |
| `__str__` | `(self)` |
| `__subclasshook__` | `No signature found` |


### Common Django Methods

| Method Name |Signature |
|-------------|----------|
| `_check_column_name_clashes` | `()` |
| `_check_constraints` | `(databases)` |
| `_check_db_table_comment` | `(databases)` |
| `_check_default_pk` | `()` |
| `_check_field_name_clashes` | `()` |
| `_check_fields` | `(**kwargs)` |
| `_check_id_field` | `()` |
| `_check_indexes` | `(databases)` |
| `_check_local_fields` | `(fields, option)` |
| `_check_long_column_names` | `(databases)` |
| `_check_m2m_through_same_relationship` | `()` |
| `_check_managers` | `(**kwargs)` |
| `_check_model` | `()` |
| `_check_model_name_db_lookup_clashes` | `()` |
| `_check_ordering` | `()` |
| `_check_property_name_related_field_accessor_clashes` | `()` |
| `_check_single_primary_key` | `()` |
| `_check_swappable` | `()` |
| `_check_unique_together` | `()` |
| `_do_insert` | `(self, manager, using, fields, returning_fields, raw)` |
| `_do_update` | `(self, base_qs, using, pk_val, values, update_fields, forced_update)` |
| `_get_FIELD_display` | `(self, field)` |
| `_get_expr_references` | `(expr)` |
| `_get_field_expression_map` | `(self, meta, exclude=None)` |
| `_get_next_or_previous_by_FIELD` | `(self, field, is_next, **kwargs)` |
| `_get_next_or_previous_in_order` | `(self, is_next)` |
| `_get_pk_val` | `(self, meta=None)` |
| `_get_unique_checks` | `(self, exclude=None, include_meta_constraints=False)` |
| `_parse_params` | `(self, *args, method_name, **kwargs)` |
| `_perform_date_checks` | `(self, date_checks)` |
| `_perform_unique_checks` | `(self, unique_checks)` |
| `_prepare_related_fields_for_save` | `(self, operation_name, fields=None)` |
| `_save_parents` | `(self, cls, using, update_fields, force_insert, updated_parents=None)` |
| `_save_table` | `(self, raw=False, cls=None, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `_set_pk_val` | `(self, value)` |
| `_validate_force_insert` | `(force_insert)` |
| `adelete` | `(self, using=None, keep_parents=False)` |
| `arefresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `asave` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `check` | `(**kwargs)` |
| `clean` | `(self)` |
| `clean_fields` | `(self, exclude=None)` |
| `date_error_message` | `(self, lookup_type, field_name, unique_for)` |
| `delete` | `(self, using=None, keep_parents=False)` |
| `from_db` | `(db, field_names, values)` |
| `full_clean` | `(self, exclude=None, validate_unique=True, validate_constraints=True)` |
| `get_constraints` | `(self)` |
| `get_deferred_fields` | `(self)` |
| `prepare_database_save` | `(self, field)` |
| `refresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `save` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `save_base` | `(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `serializable_value` | `(self, field_name)` |
| `unique_error_message` | `(self, model_class, unique_check)` |
| `validate_constraints` | `(self, exclude=None)` |
| `validate_unique` | `(self, exclude=None)` |


### Other Methods

| Method Name |Signature |
|-------------|----------|
| `get_next_by_birth_date` | `(self, *, field=<django.db.models.fields.DateField: birth_date>, is_next=True, **kwargs)` |
| `get_previous_by_birth_date` | `(self, *, field=<django.db.models.fields.DateField: birth_date>, is_next=False, **kwargs)` |


---

# example.Book

## Model Info

| Key | Value |
|-----|-------|
| Model Name | Book |
| Verbose Name | book |
| Verbose Name Plural | books |
| Docstring | <p>Example Book model.</p> |
| Is Abstract | False |
| Is Proxy | False |
| Is Managed | True |
| Ordering | [] |
| Permissions | [] |
| Default Permissions | ('add', 'change', 'delete', 'view') |
| Indexes | [] |
| Constraints | [] |
| Database Table | example_book |
| Base Manager | None |
| Default Manager | None |
| File | /home/watervize/github_jacklinke/django-model-info/tests/example/models.py |
| Starting Line Number | 88 |
| Method Resolution Order | (<class 'tests.example.models.Book'>, <class 'django.db.models.base.Model'>, <class 'django.db.models.utils.AltersData'>, <class 'object'>) |


## Fields

| Field Name | Field Type | Database Column | Database Type | Verbose Name |
|------------|------------|----------------|---------------|--------------|
| `Book_authors+` | ManyToOneRel |  | bigint |  |
| `Store_books+` | ManyToOneRel |  | bigint |  |
| `authors` | ManyToManyField | authors | through example.Book_authors | authors |
| `id (pk)` | BigAutoField | id | integer | ID |
| `publication_date` | DateField | publication_date | date | publication date |
| `publisher` | ForeignKey | publisher_id | bigint | publisher |
| `store` | ManyToManyRel |  | through example.Store_books |  |
| `title` | CharField | title | varchar(100) | title |


## Relations

| Field Name | Field Type | Database Column | Database Type | Related Model | Related Name |
|------------|------------|----------------|---------------|---------------|--------------|
| `authors` | ManyToManyField | authors | through example.Book_authors | example.Author | book_set |
| `publisher` | ForeignKey | publisher_id | bigint | example.Publisher | book_set |


## Methods

### Dunder Methods

| Method Name |Signature |
|-------------|----------|
| `__class__` | `(name, bases, attrs, **kwargs)` |
| `__delattr__` | `(self, name, /)` |
| `__dir__` | `(self, /)` |
| `__eq__` | `(self, other)` |
| `__format__` | `(self, format_spec, /)` |
| `__ge__` | `(self, value, /)` |
| `__getattribute__` | `(self, name, /)` |
| `__getstate__` | `(self)` |
| `__gt__` | `(self, value, /)` |
| `__hash__` | `(self)` |
| `__init__` | `(self, *args, **kwargs)` |
| `__init_subclass__` | `(**kwargs)` |
| `__le__` | `(self, value, /)` |
| `__lt__` | `(self, value, /)` |
| `__ne__` | `(self, value, /)` |
| `__new__` | `(*args, **kwargs)` |
| `__reduce__` | `(self)` |
| `__reduce_ex__` | `(self, protocol, /)` |
| `__repr__` | `(self)` |
| `__setattr__` | `(self, name, value, /)` |
| `__setstate__` | `(self, state)` |
| `__sizeof__` | `(self, /)` |
| `__str__` | `(self)` |
| `__subclasshook__` | `No signature found` |


### Common Django Methods

| Method Name |Signature |
|-------------|----------|
| `_check_column_name_clashes` | `()` |
| `_check_constraints` | `(databases)` |
| `_check_db_table_comment` | `(databases)` |
| `_check_default_pk` | `()` |
| `_check_field_name_clashes` | `()` |
| `_check_fields` | `(**kwargs)` |
| `_check_id_field` | `()` |
| `_check_indexes` | `(databases)` |
| `_check_local_fields` | `(fields, option)` |
| `_check_long_column_names` | `(databases)` |
| `_check_m2m_through_same_relationship` | `()` |
| `_check_managers` | `(**kwargs)` |
| `_check_model` | `()` |
| `_check_model_name_db_lookup_clashes` | `()` |
| `_check_ordering` | `()` |
| `_check_property_name_related_field_accessor_clashes` | `()` |
| `_check_single_primary_key` | `()` |
| `_check_swappable` | `()` |
| `_check_unique_together` | `()` |
| `_do_insert` | `(self, manager, using, fields, returning_fields, raw)` |
| `_do_update` | `(self, base_qs, using, pk_val, values, update_fields, forced_update)` |
| `_get_FIELD_display` | `(self, field)` |
| `_get_expr_references` | `(expr)` |
| `_get_field_expression_map` | `(self, meta, exclude=None)` |
| `_get_next_or_previous_by_FIELD` | `(self, field, is_next, **kwargs)` |
| `_get_next_or_previous_in_order` | `(self, is_next)` |
| `_get_pk_val` | `(self, meta=None)` |
| `_get_unique_checks` | `(self, exclude=None, include_meta_constraints=False)` |
| `_parse_params` | `(self, *args, method_name, **kwargs)` |
| `_perform_date_checks` | `(self, date_checks)` |
| `_perform_unique_checks` | `(self, unique_checks)` |
| `_prepare_related_fields_for_save` | `(self, operation_name, fields=None)` |
| `_save_parents` | `(self, cls, using, update_fields, force_insert, updated_parents=None)` |
| `_save_table` | `(self, raw=False, cls=None, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `_set_pk_val` | `(self, value)` |
| `_validate_force_insert` | `(force_insert)` |
| `adelete` | `(self, using=None, keep_parents=False)` |
| `arefresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `asave` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `check` | `(**kwargs)` |
| `clean` | `(self)` |
| `clean_fields` | `(self, exclude=None)` |
| `date_error_message` | `(self, lookup_type, field_name, unique_for)` |
| `delete` | `(self, using=None, keep_parents=False)` |
| `from_db` | `(db, field_names, values)` |
| `full_clean` | `(self, exclude=None, validate_unique=True, validate_constraints=True)` |
| `get_constraints` | `(self)` |
| `get_deferred_fields` | `(self)` |
| `prepare_database_save` | `(self, field)` |
| `refresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `save` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `save_base` | `(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `serializable_value` | `(self, field_name)` |
| `unique_error_message` | `(self, model_class, unique_check)` |
| `validate_constraints` | `(self, exclude=None)` |
| `validate_unique` | `(self, exclude=None)` |


### Other Methods

| Method Name |Signature |
|-------------|----------|
| `get_authors` | `(self)` |
| `get_next_by_publication_date` | `(self, *, field=<django.db.models.fields.DateField: publication_date>, is_next=True, **kwargs)` |
| `get_previous_by_publication_date` | `(self, *, field=<django.db.models.fields.DateField: publication_date>, is_next=False, **kwargs)` |


---

# example.ConcreteProfile

## Model Info

| Key | Value |
|-----|-------|
| Model Name | ConcreteProfile |
| Verbose Name | User Profile |
| Verbose Name Plural | User Profiles |
| Docstring | <p>Example ConcreteProfile model.</p> |
| Is Abstract | False |
| Is Proxy | False |
| Is Managed | True |
| Ordering | ['user__username'] |
| Permissions | [] |
| Default Permissions | ('add', 'change', 'delete', 'view') |
| Indexes | [] |
| Constraints | [] |
| Database Table | profiles |
| Database Table Comment | Table for storing user profiles |
| Database Tablespace | profiles_tablespace |
| Base Manager | None |
| Default Manager | None |
| File | /home/watervize/github_jacklinke/django-model-info/tests/example/models.py |
| Starting Line Number | 145 |
| Method Resolution Order | (<class 'tests.example.models.ConcreteProfile'>, <class 'tests.example.models.Profile'>, <class 'django.db.models.base.Model'>, <class 'django.db.models.utils.AltersData'>, <class 'object'>) |


## Fields

| Field Name | Field Type | Database Column | Database Type | Verbose Name |
|------------|------------|----------------|---------------|--------------|
| `bio` | TextField | bio | text | bio |
| `birth_date` | DateField | birth_date | date | birth date |
| `created_at` | DateTimeField | created_at | datetime | created at |
| `email` | EmailField | email | varchar(254) | email |
| `id (pk)` | BigAutoField | id | integer | ID |
| `updated_at` | DateTimeField | updated_at | datetime | updated at |
| `user` | OneToOneField | user_id | integer | user |
| `website` | URLField | website | varchar(200) | website |


## Relations

| Field Name | Field Type | Database Column | Database Type | Related Model | Related Name |
|------------|------------|----------------|---------------|---------------|--------------|
| `user` | OneToOneField | user_id | integer | auth.User | profile |


## Methods

### Dunder Methods

| Method Name |Signature |
|-------------|----------|
| `__class__` | `(name, bases, attrs, **kwargs)` |
| `__delattr__` | `(self, name, /)` |
| `__dir__` | `(self, /)` |
| `__eq__` | `(self, other)` |
| `__format__` | `(self, format_spec, /)` |
| `__ge__` | `(self, value, /)` |
| `__getattribute__` | `(self, name, /)` |
| `__getstate__` | `(self)` |
| `__gt__` | `(self, value, /)` |
| `__hash__` | `(self)` |
| `__init__` | `(self, *args, **kwargs)` |
| `__init_subclass__` | `(**kwargs)` |
| `__le__` | `(self, value, /)` |
| `__lt__` | `(self, value, /)` |
| `__ne__` | `(self, value, /)` |
| `__new__` | `(*args, **kwargs)` |
| `__reduce__` | `(self)` |
| `__reduce_ex__` | `(self, protocol, /)` |
| `__repr__` | `(self)` |
| `__setattr__` | `(self, name, value, /)` |
| `__setstate__` | `(self, state)` |
| `__sizeof__` | `(self, /)` |
| `__str__` | `(self)` |
| `__subclasshook__` | `No signature found` |


### Common Django Methods

| Method Name |Signature |
|-------------|----------|
| `_check_column_name_clashes` | `()` |
| `_check_constraints` | `(databases)` |
| `_check_db_table_comment` | `(databases)` |
| `_check_default_pk` | `()` |
| `_check_field_name_clashes` | `()` |
| `_check_fields` | `(**kwargs)` |
| `_check_id_field` | `()` |
| `_check_indexes` | `(databases)` |
| `_check_local_fields` | `(fields, option)` |
| `_check_long_column_names` | `(databases)` |
| `_check_m2m_through_same_relationship` | `()` |
| `_check_managers` | `(**kwargs)` |
| `_check_model` | `()` |
| `_check_model_name_db_lookup_clashes` | `()` |
| `_check_ordering` | `()` |
| `_check_property_name_related_field_accessor_clashes` | `()` |
| `_check_single_primary_key` | `()` |
| `_check_swappable` | `()` |
| `_check_unique_together` | `()` |
| `_do_insert` | `(self, manager, using, fields, returning_fields, raw)` |
| `_do_update` | `(self, base_qs, using, pk_val, values, update_fields, forced_update)` |
| `_get_FIELD_display` | `(self, field)` |
| `_get_expr_references` | `(expr)` |
| `_get_field_expression_map` | `(self, meta, exclude=None)` |
| `_get_next_or_previous_by_FIELD` | `(self, field, is_next, **kwargs)` |
| `_get_next_or_previous_in_order` | `(self, is_next)` |
| `_get_pk_val` | `(self, meta=None)` |
| `_get_unique_checks` | `(self, exclude=None, include_meta_constraints=False)` |
| `_parse_params` | `(self, *args, method_name, **kwargs)` |
| `_perform_date_checks` | `(self, date_checks)` |
| `_perform_unique_checks` | `(self, unique_checks)` |
| `_prepare_related_fields_for_save` | `(self, operation_name, fields=None)` |
| `_save_parents` | `(self, cls, using, update_fields, force_insert, updated_parents=None)` |
| `_save_table` | `(self, raw=False, cls=None, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `_set_pk_val` | `(self, value)` |
| `_validate_force_insert` | `(force_insert)` |
| `adelete` | `(self, using=None, keep_parents=False)` |
| `arefresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `asave` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `check` | `(**kwargs)` |
| `clean` | `(self)` |
| `clean_fields` | `(self, exclude=None)` |
| `date_error_message` | `(self, lookup_type, field_name, unique_for)` |
| `delete` | `(self, using=None, keep_parents=False)` |
| `from_db` | `(db, field_names, values)` |
| `full_clean` | `(self, exclude=None, validate_unique=True, validate_constraints=True)` |
| `get_constraints` | `(self)` |
| `get_deferred_fields` | `(self)` |
| `prepare_database_save` | `(self, field)` |
| `refresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `save` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `save_base` | `(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `serializable_value` | `(self, field_name)` |
| `unique_error_message` | `(self, model_class, unique_check)` |
| `validate_constraints` | `(self, exclude=None)` |
| `validate_unique` | `(self, exclude=None)` |


### Private Methods

| Method Name |Signature |
|-------------|----------|
| `_some_private_method` | `(self)` |


### Other Methods

| Method Name |Signature |
|-------------|----------|
| `get_next_by_birth_date` | `(self, *, field=<django.db.models.fields.DateField: birth_date>, is_next=True, **kwargs)` |
| `get_next_by_created_at` | `(self, *, field=<django.db.models.fields.DateTimeField: created_at>, is_next=True, **kwargs)` |
| `get_next_by_updated_at` | `(self, *, field=<django.db.models.fields.DateTimeField: updated_at>, is_next=True, **kwargs)` |
| `get_previous_by_birth_date` | `(self, *, field=<django.db.models.fields.DateField: birth_date>, is_next=False, **kwargs)` |
| `get_previous_by_created_at` | `(self, *, field=<django.db.models.fields.DateTimeField: created_at>, is_next=False, **kwargs)` |
| `get_previous_by_updated_at` | `(self, *, field=<django.db.models.fields.DateTimeField: updated_at>, is_next=False, **kwargs)` |


---

# example.Publisher

## Model Info

| Key | Value |
|-----|-------|
| Model Name | Publisher |
| Verbose Name | publisher |
| Verbose Name Plural | publishers |
| Docstring | <p>Example Publisher model.</p> |
| Is Abstract | False |
| Is Proxy | False |
| Is Managed | True |
| Ordering | [] |
| Permissions | [] |
| Default Permissions | ('add', 'change', 'delete', 'view') |
| Indexes | [] |
| Constraints | [] |
| Database Table | example_publisher |
| Base Manager | None |
| Default Manager | None |
| File | /home/watervize/github_jacklinke/django-model-info/tests/example/models.py |
| Starting Line Number | 74 |
| Method Resolution Order | (<class 'tests.example.models.Publisher'>, <class 'django.db.models.base.Model'>, <class 'django.db.models.utils.AltersData'>, <class 'object'>) |


## Fields

| Field Name | Field Type | Database Column | Database Type | Verbose Name |
|------------|------------|----------------|---------------|--------------|
| `address` | CharField | address | varchar(255) | address |
| `book` | ManyToOneRel |  | bigint |  |
| `city` | CharField | city | varchar(60) | city |
| `country` | CharField | country | varchar(50) | country |
| `id (pk)` | BigAutoField | id | integer | ID |
| `name` | CharField | name | varchar(100) | name |
| `state_province` | CharField | state_province | varchar(30) | state province |
| `website` | URLField | website | varchar(200) | website |


## Methods

### Dunder Methods

| Method Name |Signature |
|-------------|----------|
| `__class__` | `(name, bases, attrs, **kwargs)` |
| `__delattr__` | `(self, name, /)` |
| `__dir__` | `(self, /)` |
| `__eq__` | `(self, other)` |
| `__format__` | `(self, format_spec, /)` |
| `__ge__` | `(self, value, /)` |
| `__getattribute__` | `(self, name, /)` |
| `__getstate__` | `(self)` |
| `__gt__` | `(self, value, /)` |
| `__hash__` | `(self)` |
| `__init__` | `(self, *args, **kwargs)` |
| `__init_subclass__` | `(**kwargs)` |
| `__le__` | `(self, value, /)` |
| `__lt__` | `(self, value, /)` |
| `__ne__` | `(self, value, /)` |
| `__new__` | `(*args, **kwargs)` |
| `__reduce__` | `(self)` |
| `__reduce_ex__` | `(self, protocol, /)` |
| `__repr__` | `(self)` |
| `__setattr__` | `(self, name, value, /)` |
| `__setstate__` | `(self, state)` |
| `__sizeof__` | `(self, /)` |
| `__str__` | `(self)` |
| `__subclasshook__` | `No signature found` |


### Common Django Methods

| Method Name |Signature |
|-------------|----------|
| `_check_column_name_clashes` | `()` |
| `_check_constraints` | `(databases)` |
| `_check_db_table_comment` | `(databases)` |
| `_check_default_pk` | `()` |
| `_check_field_name_clashes` | `()` |
| `_check_fields` | `(**kwargs)` |
| `_check_id_field` | `()` |
| `_check_indexes` | `(databases)` |
| `_check_local_fields` | `(fields, option)` |
| `_check_long_column_names` | `(databases)` |
| `_check_m2m_through_same_relationship` | `()` |
| `_check_managers` | `(**kwargs)` |
| `_check_model` | `()` |
| `_check_model_name_db_lookup_clashes` | `()` |
| `_check_ordering` | `()` |
| `_check_property_name_related_field_accessor_clashes` | `()` |
| `_check_single_primary_key` | `()` |
| `_check_swappable` | `()` |
| `_check_unique_together` | `()` |
| `_do_insert` | `(self, manager, using, fields, returning_fields, raw)` |
| `_do_update` | `(self, base_qs, using, pk_val, values, update_fields, forced_update)` |
| `_get_FIELD_display` | `(self, field)` |
| `_get_expr_references` | `(expr)` |
| `_get_field_expression_map` | `(self, meta, exclude=None)` |
| `_get_next_or_previous_by_FIELD` | `(self, field, is_next, **kwargs)` |
| `_get_next_or_previous_in_order` | `(self, is_next)` |
| `_get_pk_val` | `(self, meta=None)` |
| `_get_unique_checks` | `(self, exclude=None, include_meta_constraints=False)` |
| `_parse_params` | `(self, *args, method_name, **kwargs)` |
| `_perform_date_checks` | `(self, date_checks)` |
| `_perform_unique_checks` | `(self, unique_checks)` |
| `_prepare_related_fields_for_save` | `(self, operation_name, fields=None)` |
| `_save_parents` | `(self, cls, using, update_fields, force_insert, updated_parents=None)` |
| `_save_table` | `(self, raw=False, cls=None, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `_set_pk_val` | `(self, value)` |
| `_validate_force_insert` | `(force_insert)` |
| `adelete` | `(self, using=None, keep_parents=False)` |
| `arefresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `asave` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `check` | `(**kwargs)` |
| `clean` | `(self)` |
| `clean_fields` | `(self, exclude=None)` |
| `date_error_message` | `(self, lookup_type, field_name, unique_for)` |
| `delete` | `(self, using=None, keep_parents=False)` |
| `from_db` | `(db, field_names, values)` |
| `full_clean` | `(self, exclude=None, validate_unique=True, validate_constraints=True)` |
| `get_constraints` | `(self)` |
| `get_deferred_fields` | `(self)` |
| `prepare_database_save` | `(self, field)` |
| `refresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `save` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `save_base` | `(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `serializable_value` | `(self, field_name)` |
| `unique_error_message` | `(self, model_class, unique_check)` |
| `validate_constraints` | `(self, exclude=None)` |
| `validate_unique` | `(self, exclude=None)` |


---

# example.Store

## Model Info

| Key | Value |
|-----|-------|
| Model Name | Store |
| Verbose Name | store |
| Verbose Name Plural | stores |
| Docstring | <p>Example Store model.</p> |
| Is Abstract | False |
| Is Proxy | False |
| Is Managed | True |
| Ordering | [] |
| Permissions | [] |
| Default Permissions | ('add', 'change', 'delete', 'view') |
| Indexes | [] |
| Constraints | [] |
| Database Table | example_store |
| Base Manager | None |
| Default Manager | None |
| File | /home/watervize/github_jacklinke/django-model-info/tests/example/models.py |
| Starting Line Number | 104 |
| Method Resolution Order | (<class 'tests.example.models.Store'>, <class 'django.db.models.base.Model'>, <class 'django.db.models.utils.AltersData'>, <class 'object'>) |


## Fields

| Field Name | Field Type | Database Column | Database Type | Verbose Name |
|------------|------------|----------------|---------------|--------------|
| `Store_books+` | ManyToOneRel |  | bigint |  |
| `books` | ManyToManyField | books | through example.Store_books | books |
| `id (pk)` | BigAutoField | id | integer | ID |
| `location` | CharField | location | varchar(100) | location |
| `name` | CharField | name | varchar(100) | name |


## Relations

| Field Name | Field Type | Database Column | Database Type | Related Model | Related Name |
|------------|------------|----------------|---------------|---------------|--------------|
| `books` | ManyToManyField | books | through example.Store_books | example.Book | store_set |


## Methods

### Dunder Methods

| Method Name |Signature |
|-------------|----------|
| `__class__` | `(name, bases, attrs, **kwargs)` |
| `__delattr__` | `(self, name, /)` |
| `__dir__` | `(self, /)` |
| `__eq__` | `(self, other)` |
| `__format__` | `(self, format_spec, /)` |
| `__ge__` | `(self, value, /)` |
| `__getattribute__` | `(self, name, /)` |
| `__getstate__` | `(self)` |
| `__gt__` | `(self, value, /)` |
| `__hash__` | `(self)` |
| `__init__` | `(self, *args, **kwargs)` |
| `__init_subclass__` | `(**kwargs)` |
| `__le__` | `(self, value, /)` |
| `__lt__` | `(self, value, /)` |
| `__ne__` | `(self, value, /)` |
| `__new__` | `(*args, **kwargs)` |
| `__reduce__` | `(self)` |
| `__reduce_ex__` | `(self, protocol, /)` |
| `__repr__` | `(self)` |
| `__setattr__` | `(self, name, value, /)` |
| `__setstate__` | `(self, state)` |
| `__sizeof__` | `(self, /)` |
| `__str__` | `(self)` |
| `__subclasshook__` | `No signature found` |


### Common Django Methods

| Method Name |Signature |
|-------------|----------|
| `_check_column_name_clashes` | `()` |
| `_check_constraints` | `(databases)` |
| `_check_db_table_comment` | `(databases)` |
| `_check_default_pk` | `()` |
| `_check_field_name_clashes` | `()` |
| `_check_fields` | `(**kwargs)` |
| `_check_id_field` | `()` |
| `_check_indexes` | `(databases)` |
| `_check_local_fields` | `(fields, option)` |
| `_check_long_column_names` | `(databases)` |
| `_check_m2m_through_same_relationship` | `()` |
| `_check_managers` | `(**kwargs)` |
| `_check_model` | `()` |
| `_check_model_name_db_lookup_clashes` | `()` |
| `_check_ordering` | `()` |
| `_check_property_name_related_field_accessor_clashes` | `()` |
| `_check_single_primary_key` | `()` |
| `_check_swappable` | `()` |
| `_check_unique_together` | `()` |
| `_do_insert` | `(self, manager, using, fields, returning_fields, raw)` |
| `_do_update` | `(self, base_qs, using, pk_val, values, update_fields, forced_update)` |
| `_get_FIELD_display` | `(self, field)` |
| `_get_expr_references` | `(expr)` |
| `_get_field_expression_map` | `(self, meta, exclude=None)` |
| `_get_next_or_previous_by_FIELD` | `(self, field, is_next, **kwargs)` |
| `_get_next_or_previous_in_order` | `(self, is_next)` |
| `_get_pk_val` | `(self, meta=None)` |
| `_get_unique_checks` | `(self, exclude=None, include_meta_constraints=False)` |
| `_parse_params` | `(self, *args, method_name, **kwargs)` |
| `_perform_date_checks` | `(self, date_checks)` |
| `_perform_unique_checks` | `(self, unique_checks)` |
| `_prepare_related_fields_for_save` | `(self, operation_name, fields=None)` |
| `_save_parents` | `(self, cls, using, update_fields, force_insert, updated_parents=None)` |
| `_save_table` | `(self, raw=False, cls=None, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `_set_pk_val` | `(self, value)` |
| `_validate_force_insert` | `(force_insert)` |
| `adelete` | `(self, using=None, keep_parents=False)` |
| `arefresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `asave` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `check` | `(**kwargs)` |
| `clean` | `(self)` |
| `clean_fields` | `(self, exclude=None)` |
| `date_error_message` | `(self, lookup_type, field_name, unique_for)` |
| `delete` | `(self, using=None, keep_parents=False)` |
| `from_db` | `(db, field_names, values)` |
| `full_clean` | `(self, exclude=None, validate_unique=True, validate_constraints=True)` |
| `get_constraints` | `(self)` |
| `get_deferred_fields` | `(self)` |
| `prepare_database_save` | `(self, field)` |
| `refresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `save` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `save_base` | `(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `serializable_value` | `(self, field_name)` |
| `unique_error_message` | `(self, model_class, unique_check)` |
| `validate_constraints` | `(self, exclude=None)` |
| `validate_unique` | `(self, exclude=None)` |


### Other Methods

| Method Name |Signature |
|-------------|----------|
| `get_books` | `(self)` |
| `get_books_with_author` | `(self, author: str)` |


---

# example.UnmanagedAuthor

## Model Info

| Key | Value |
|-----|-------|
| Model Name | UnmanagedAuthor |
| Verbose Name | unmanaged author |
| Verbose Name Plural | unmanaged authors |
| Docstring | <p>Example UnmanagedAuthor model.</p> |
| Is Abstract | False |
| Is Proxy | False |
| Is Managed | True |
| Ordering | [] |
| Permissions | [] |
| Default Permissions | ('add', 'change', 'delete', 'view') |
| Indexes | [] |
| Constraints | [] |
| Database Table | example_unmanagedauthor |
| Base Manager | None |
| Default Manager | None |
| File | /home/watervize/github_jacklinke/django-model-info/tests/example/models.py |
| Starting Line Number | 58 |
| Method Resolution Order | (<class 'tests.example.models.UnmanagedAuthor'>, <class 'django.db.models.base.Model'>, <class 'django.db.models.utils.AltersData'>, <class 'object'>) |


## Fields

| Field Name | Field Type | Database Column | Database Type | Verbose Name |
|------------|------------|----------------|---------------|--------------|
| `birth_date` | DateField | birth_date | date | birth date |
| `first_name` | CharField | first_name | varchar(50) | first name |
| `id (pk)` | BigAutoField | id | integer | ID |
| `last_name` | CharField | last_name | varchar(50) | last name |


## Methods

### Dunder Methods

| Method Name |Signature |
|-------------|----------|
| `__class__` | `(name, bases, attrs, **kwargs)` |
| `__delattr__` | `(self, name, /)` |
| `__dir__` | `(self, /)` |
| `__eq__` | `(self, other)` |
| `__format__` | `(self, format_spec, /)` |
| `__ge__` | `(self, value, /)` |
| `__getattribute__` | `(self, name, /)` |
| `__getstate__` | `(self)` |
| `__gt__` | `(self, value, /)` |
| `__hash__` | `(self)` |
| `__init__` | `(self, *args, **kwargs)` |
| `__init_subclass__` | `(**kwargs)` |
| `__le__` | `(self, value, /)` |
| `__lt__` | `(self, value, /)` |
| `__ne__` | `(self, value, /)` |
| `__new__` | `(*args, **kwargs)` |
| `__reduce__` | `(self)` |
| `__reduce_ex__` | `(self, protocol, /)` |
| `__repr__` | `(self)` |
| `__setattr__` | `(self, name, value, /)` |
| `__setstate__` | `(self, state)` |
| `__sizeof__` | `(self, /)` |
| `__str__` | `(self)` |
| `__subclasshook__` | `No signature found` |


### Common Django Methods

| Method Name |Signature |
|-------------|----------|
| `_check_column_name_clashes` | `()` |
| `_check_constraints` | `(databases)` |
| `_check_db_table_comment` | `(databases)` |
| `_check_default_pk` | `()` |
| `_check_field_name_clashes` | `()` |
| `_check_fields` | `(**kwargs)` |
| `_check_id_field` | `()` |
| `_check_indexes` | `(databases)` |
| `_check_local_fields` | `(fields, option)` |
| `_check_long_column_names` | `(databases)` |
| `_check_m2m_through_same_relationship` | `()` |
| `_check_managers` | `(**kwargs)` |
| `_check_model` | `()` |
| `_check_model_name_db_lookup_clashes` | `()` |
| `_check_ordering` | `()` |
| `_check_property_name_related_field_accessor_clashes` | `()` |
| `_check_single_primary_key` | `()` |
| `_check_swappable` | `()` |
| `_check_unique_together` | `()` |
| `_do_insert` | `(self, manager, using, fields, returning_fields, raw)` |
| `_do_update` | `(self, base_qs, using, pk_val, values, update_fields, forced_update)` |
| `_get_FIELD_display` | `(self, field)` |
| `_get_expr_references` | `(expr)` |
| `_get_field_expression_map` | `(self, meta, exclude=None)` |
| `_get_next_or_previous_by_FIELD` | `(self, field, is_next, **kwargs)` |
| `_get_next_or_previous_in_order` | `(self, is_next)` |
| `_get_pk_val` | `(self, meta=None)` |
| `_get_unique_checks` | `(self, exclude=None, include_meta_constraints=False)` |
| `_parse_params` | `(self, *args, method_name, **kwargs)` |
| `_perform_date_checks` | `(self, date_checks)` |
| `_perform_unique_checks` | `(self, unique_checks)` |
| `_prepare_related_fields_for_save` | `(self, operation_name, fields=None)` |
| `_save_parents` | `(self, cls, using, update_fields, force_insert, updated_parents=None)` |
| `_save_table` | `(self, raw=False, cls=None, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `_set_pk_val` | `(self, value)` |
| `_validate_force_insert` | `(force_insert)` |
| `adelete` | `(self, using=None, keep_parents=False)` |
| `arefresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `asave` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `check` | `(**kwargs)` |
| `clean` | `(self)` |
| `clean_fields` | `(self, exclude=None)` |
| `date_error_message` | `(self, lookup_type, field_name, unique_for)` |
| `delete` | `(self, using=None, keep_parents=False)` |
| `from_db` | `(db, field_names, values)` |
| `full_clean` | `(self, exclude=None, validate_unique=True, validate_constraints=True)` |
| `get_constraints` | `(self)` |
| `get_deferred_fields` | `(self)` |
| `prepare_database_save` | `(self, field)` |
| `refresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `save` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `save_base` | `(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `serializable_value` | `(self, field_name)` |
| `unique_error_message` | `(self, model_class, unique_check)` |
| `validate_constraints` | `(self, exclude=None)` |
| `validate_unique` | `(self, exclude=None)` |


### Other Methods

| Method Name |Signature |
|-------------|----------|
| `get_next_by_birth_date` | `(self, *, field=<django.db.models.fields.DateField: birth_date>, is_next=True, **kwargs)` |
| `get_previous_by_birth_date` | `(self, *, field=<django.db.models.fields.DateField: birth_date>, is_next=False, **kwargs)` |


---

# sessions.Session

## Model Info

| Key | Value |
|-----|-------|
| Model Name | Session |
| Verbose Name | session |
| Verbose Name Plural | sessions |
| Docstring | <p>Django provides full support for anonymous sessions. The session<br>framework lets you store and retrieve arbitrary data on a<br>per-site-visitor basis. It stores data on the server side and<br>abstracts the sending and receiving of cookies. Cookies contain a<br>session ID -- not the data itself.</p><p>The Django sessions framework is entirely cookie-based. It does<br>not fall back to putting session IDs in URLs. This is an intentional<br>design decision. Not only does that behavior make URLs ugly, it makes<br>your site vulnerable to session-ID theft via the "Referer" header.</p><p>For complete documentation on using Sessions in your code, consult<br>the sessions documentation that is shipped with Django (also available<br>on the Django web site).</p> |
| Is Abstract | False |
| Is Proxy | False |
| Is Managed | True |
| Ordering | [] |
| Permissions | [] |
| Default Permissions | ('add', 'change', 'delete', 'view') |
| Indexes | [] |
| Constraints | [] |
| Database Table | django_session |
| Base Manager | None |
| Default Manager | None |
| File | /home/watervize/github_jacklinke/django-model-info/.venv/lib/python3.11/site-packages/django/contrib/sessions/models.py |
| Starting Line Number | 8 |
| Method Resolution Order | (<class 'django.contrib.sessions.models.Session'>, <class 'django.contrib.sessions.base_session.AbstractBaseSession'>, <class 'django.db.models.base.Model'>, <class 'django.db.models.utils.AltersData'>, <class 'object'>) |


## Fields

| Field Name | Field Type | Database Column | Database Type | Verbose Name |
|------------|------------|----------------|---------------|--------------|
| `expire_date` | DateTimeField | expire_date | datetime | expire date |
| `session_data` | TextField | session_data | text | session data |
| `session_key (pk)` | CharField | session_key | varchar(40) | session key |


## Methods

### Dunder Methods

| Method Name |Signature |
|-------------|----------|
| `__class__` | `(name, bases, attrs, **kwargs)` |
| `__delattr__` | `(self, name, /)` |
| `__dir__` | `(self, /)` |
| `__eq__` | `(self, other)` |
| `__format__` | `(self, format_spec, /)` |
| `__ge__` | `(self, value, /)` |
| `__getattribute__` | `(self, name, /)` |
| `__getstate__` | `(self)` |
| `__gt__` | `(self, value, /)` |
| `__hash__` | `(self)` |
| `__init__` | `(self, *args, **kwargs)` |
| `__init_subclass__` | `(**kwargs)` |
| `__le__` | `(self, value, /)` |
| `__lt__` | `(self, value, /)` |
| `__ne__` | `(self, value, /)` |
| `__new__` | `(*args, **kwargs)` |
| `__reduce__` | `(self)` |
| `__reduce_ex__` | `(self, protocol, /)` |
| `__repr__` | `(self)` |
| `__setattr__` | `(self, name, value, /)` |
| `__setstate__` | `(self, state)` |
| `__sizeof__` | `(self, /)` |
| `__str__` | `(self)` |
| `__subclasshook__` | `No signature found` |


### Common Django Methods

| Method Name |Signature |
|-------------|----------|
| `_check_column_name_clashes` | `()` |
| `_check_constraints` | `(databases)` |
| `_check_db_table_comment` | `(databases)` |
| `_check_default_pk` | `()` |
| `_check_field_name_clashes` | `()` |
| `_check_fields` | `(**kwargs)` |
| `_check_id_field` | `()` |
| `_check_indexes` | `(databases)` |
| `_check_local_fields` | `(fields, option)` |
| `_check_long_column_names` | `(databases)` |
| `_check_m2m_through_same_relationship` | `()` |
| `_check_managers` | `(**kwargs)` |
| `_check_model` | `()` |
| `_check_model_name_db_lookup_clashes` | `()` |
| `_check_ordering` | `()` |
| `_check_property_name_related_field_accessor_clashes` | `()` |
| `_check_single_primary_key` | `()` |
| `_check_swappable` | `()` |
| `_check_unique_together` | `()` |
| `_do_insert` | `(self, manager, using, fields, returning_fields, raw)` |
| `_do_update` | `(self, base_qs, using, pk_val, values, update_fields, forced_update)` |
| `_get_FIELD_display` | `(self, field)` |
| `_get_expr_references` | `(expr)` |
| `_get_field_expression_map` | `(self, meta, exclude=None)` |
| `_get_next_or_previous_by_FIELD` | `(self, field, is_next, **kwargs)` |
| `_get_next_or_previous_in_order` | `(self, is_next)` |
| `_get_pk_val` | `(self, meta=None)` |
| `_get_unique_checks` | `(self, exclude=None, include_meta_constraints=False)` |
| `_parse_params` | `(self, *args, method_name, **kwargs)` |
| `_perform_date_checks` | `(self, date_checks)` |
| `_perform_unique_checks` | `(self, unique_checks)` |
| `_prepare_related_fields_for_save` | `(self, operation_name, fields=None)` |
| `_save_parents` | `(self, cls, using, update_fields, force_insert, updated_parents=None)` |
| `_save_table` | `(self, raw=False, cls=None, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `_set_pk_val` | `(self, value)` |
| `_validate_force_insert` | `(force_insert)` |
| `adelete` | `(self, using=None, keep_parents=False)` |
| `arefresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `asave` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `check` | `(**kwargs)` |
| `clean` | `(self)` |
| `clean_fields` | `(self, exclude=None)` |
| `date_error_message` | `(self, lookup_type, field_name, unique_for)` |
| `delete` | `(self, using=None, keep_parents=False)` |
| `from_db` | `(db, field_names, values)` |
| `full_clean` | `(self, exclude=None, validate_unique=True, validate_constraints=True)` |
| `get_constraints` | `(self)` |
| `get_decoded` | `(self)` |
| `get_deferred_fields` | `(self)` |
| `get_next_by_expire_date` | `(self, *, field=<django.db.models.fields.DateTimeField: expire_date>, is_next=True, **kwargs)` |
| `get_previous_by_expire_date` | `(self, *, field=<django.db.models.fields.DateTimeField: expire_date>, is_next=False, **kwargs)` |
| `get_session_store_class` | `()` |
| `prepare_database_save` | `(self, field)` |
| `refresh_from_db` | `(self, using=None, fields=None, from_queryset=None)` |
| `save` | `(self, *args, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `save_base` | `(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None)` |
| `serializable_value` | `(self, field_name)` |
| `unique_error_message` | `(self, model_class, unique_check)` |
| `validate_constraints` | `(self, exclude=None)` |
| `validate_unique` | `(self, exclude=None)` |


---
