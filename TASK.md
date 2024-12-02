# Ticket: accounts table name columns

The accounts table is replacing its `full_name` column with separate
`first_name` and `last_name` columns. The migration runs next sprint.

Anything that reads customer names from the accounts table needs updating
so that it carries on showing names as "First Last".
