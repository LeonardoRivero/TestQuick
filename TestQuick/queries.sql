SELECT
    document,
    first_name,
    last_name,
    email,
    bills.company_name
FROM
    "Rest_API_clients" AS clients
    INNER JOIN "Rest_API_bills" AS bills ON bills.client_id_id = clients.id