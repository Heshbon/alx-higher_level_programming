-- Lists all records of the table second_table.
-- Records are listed in descending order.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
