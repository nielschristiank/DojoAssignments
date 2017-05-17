/*SELECT billing.charged_datetime as month, SUM(billing.amount) as revenue_march
FROM billing
WHERE billing.charged_datetime LIKE ('%2012-03%');*/

SELECT DATE_FORMAT(billing.charged_datetime, '%M') as month, SUM(billing.amount) as revenue
FROM billing
WHERE MONTH(billing.charged_datetime) = 3 AND YEAR(billing.charged_datetime) = 2012;

SELECT clients.client_id, SUM(billing.amount) as total_billed
FROM billing
JOIN clients ON billing.client_id = clients.client_id
WHERE clients.client_id = 2;

SELECT sites.domain_name, clients.client_id
FROM sites
JOIN clients ON sites.client_id = clients.client_id
WHERE clients.client_id = 10;

SELECT clients.client_id, COUNT(sites.domain_name) as number_of_sites, DATE_FORMAT(sites.created_datetime, '%M') as month, DATE_FORMAT(sites.created_datetime, '%Y') as year
FROM sites
JOIN clients ON sites.client_id = clients.client_id
WHERE clients.client_id = 1
GROUP BY year, month;

SELECT COUNT(leads.leads_id) as num_leads, sites.domain_name, DATE_FORMAT(leads.registered_datetime, '%M %D %Y') as date_created
FROM leads
JOIN sites ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' and '2011-02-15'
GROUP BY sites.domain_name
ORDER BY leads.leads_id;

SELECT CONCAT_WS(' ', clients.first_name, clients.last_name) as client_name, COUNT(leads.leads_id) as number_of_leads
FROM leads
LEFT JOIN sites ON sites.site_id = leads.site_id
LEFT JOIN clients ON sites.client_id = clients.client_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY client_name
ORDER BY leads.registered_datetime;

SELECT CONCAT_WS(' ', clients.first_name, clients.last_name) as client_name, COUNT(leads.leads_id) as number_of_leads, DATE_FORMAT(leads.registered_datetime, '%M') as month
FROM leads
LEFT JOIN sites ON sites.site_id = leads.site_id
LEFT JOIN clients ON sites.client_id = clients.client_id
WHERE MONTH(leads.registered_datetime) BETWEEN 1 AND 6 AND YEAR(leads.registered_datetime) = 2011
GROUP BY leads.leads_id
ORDER BY leads.registered_datetime;

SELECT CONCAT_WS(' ', clients.first_name, clients.last_name) as client_name,  sites.domain_name, COUNT(leads.leads_id) as number_of_leads, DATE_FORMAT(leads.registered_datetime, '%M %D %Y')
FROM leads
JOIN sites ON sites.site_id = leads.site_id
JOIN clients ON sites.client_id = clients.client_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY sites.domain_name
ORDER BY clients.client_id;

SELECT CONCAT_WS(' ', clients.first_name, clients.last_name) as client_name,  sites.domain_name, COUNT(leads.leads_id) as number_of_leads
FROM leads
JOIN sites ON sites.site_id = leads.site_id
JOIN clients ON sites.client_id = clients.client_id
GROUP BY sites.domain_name
ORDER BY clients.client_id;

SELECT CONCAT_WS(' ', clients.first_name, clients.last_name) as client_name, SUM(billing.amount) as total_revenue, DATE_FORMAT(billing.charged_datetime, '%M') as month, DATE_FORMAT(billing.charged_datetime, '%Y') as year
FROM billing
JOIN clients ON billing.client_id = clients.client_id
GROUP BY clients.client_id, month, year
ORDER BY clients.client_id, billing.charged_datetime;

SELECT CONCAT_WS(' ', clients.first_name, clients.last_name) as client_name, GROUP_CONCAT(sites.domain_name SEPARATOR ' / ') as domains_owned
FROM sites
JOIN clients ON sites.client_id = clients.client_id
GROUP BY clients.client_id;


