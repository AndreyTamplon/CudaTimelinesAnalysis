SELECT start, end, srcDeviceId, dstDeviceId, bytes
FROM CUPTI_ACTIVITY_KIND_MEMCPY
ORDER BY start;