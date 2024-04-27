-- list all bands with style glam rock
SELECT band_name, COALESCE(split - formed, 2022 - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
