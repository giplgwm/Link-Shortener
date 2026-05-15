-- :name insert_link :insert
INSERT INTO links (url, slug, created_by)
VALUES (:url, :slug, :created_by);