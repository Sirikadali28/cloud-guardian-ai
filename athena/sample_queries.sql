SELECT *
FROM cloud_guardian_findings
LIMIT 10;


SELECT severity,
COUNT(*) as total_findings
FROM cloud_guardian_findings
GROUP BY severity;


SELECT issue,
COUNT(*) as occurrences
FROM cloud_guardian_findings
GROUP BY issue;