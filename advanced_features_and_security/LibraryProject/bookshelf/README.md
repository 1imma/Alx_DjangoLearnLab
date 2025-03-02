# Permissions and Groups Setup

This application uses Django's built-in permissions and groups to control access to specific actions.

## Permissions
The following custom permissions are defined in the `Book` model:
- `can_view`: Allows viewing books.
- `can_create`: Allows creating books.
- `can_edit`: Allows editing books.
- `can_delete`: Allows deleting books.

## Groups
The following groups are created and assigned permissions:
- **Viewers**: Can view books.
- **Editors**: Can view, create, and edit books.
- **Admins**: Can view, create, edit, and delete books.

## Enforcing Permissions
Permissions are enforced in views using the `@permission_required` decorator. For example:
- `@permission_required('advanced_features_and_security.can_edit')` ensures only users with the `can_edit` permission can access the view.

## Testing
1. Create test users and assign them to groups.
2. Log in as each user and verify that permissions are enforced correctly.