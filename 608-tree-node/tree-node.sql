-- Write your PostgreSQL query statement below
SELECT id, 'Root' as type
FROM Tree
WHERE p_id IS NULL
UNION
SELECT id, 'Inner' as type
FROM TREE
WHERE id in (SELECT p_id FROM Tree WHERE p_id IS NOT NULL) AND p_id IS NOT NULL

UNION
SELECT id, 'Leaf' as type
FROM TREE
WHERE id NOT IN (SELECT p_id FROM Tree WHERE p_id IS NOT NULL) AND p_id IS NOT NULL
ORDER BY id

