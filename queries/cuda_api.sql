SELECT start, s.value
FROM CUPTI_ACTIVITY_KIND_RUNTIME a LEFT OUTER JOIN StringIds s ON a.nameId = s.id
ORDER BY start
