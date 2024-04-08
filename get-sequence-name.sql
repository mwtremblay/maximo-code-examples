-- Quickly get the sequence name used on a Maximo attribute while working in your SQL tool

SELECT
  tbname,
  name,
  sequencename
FROM 
  maxsequence
WHERE
  tbname = :tbname -- table/object name
  AND name = :name -- column/attribute name
;