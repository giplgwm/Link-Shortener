-- :name get_link :one
SELECT url FROM links WHERE slug = :slug;