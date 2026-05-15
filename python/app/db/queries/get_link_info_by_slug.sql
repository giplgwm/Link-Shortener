-- :name get_link_info :one
SELECT * FROM links WHERE slug = :slug;