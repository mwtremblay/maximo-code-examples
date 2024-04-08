-- Quickly get the primary key for a Maximo object while working in your SQL tool

SELECT
  objectname,
  attributename,
  primarykeycolseq
FROM
  maxattributecfg
WHERE 
  objectname = :objectname
;