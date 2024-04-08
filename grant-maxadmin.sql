-- If you are testing something and have to pull yourself out of the MAXADMIN group and can't bug someone to put you back in.

INSERT
  INTO groupuser (
    groupuserid,
    userid,
    groupname)
  VALUES (
    groupuserseq.nextval,
    upper(:userid),
    'MAXADMIN')
;

COMMIT;