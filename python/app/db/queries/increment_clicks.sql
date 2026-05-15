-- :name increment_clicks :affected
UPDATE links SET clicks = clicks + 1 WHERE slug = :slug;