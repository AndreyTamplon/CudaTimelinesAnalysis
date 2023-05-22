SELECT start, end, s.value
FROM CUPTI_ACTIVITY_KIND_KERNEL k LEFT OUTER JOIN StringIds s ON k.demangledName = s.id
ORDER BY start
LIMIT 500