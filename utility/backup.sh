#back up feeds
#mysqldump -hhaiyangxu.cyhw0vc2x53y.ap-southeast-1.rds.amazonaws.com -uhaiyangxu -phaiyangxu insights feeds>feeds.sql

#import
mysql -hhaiyangxu.cyhw0vc2x53y.ap-southeast-1.rds.amazonaws.com -uhaiyangxu -phaiyangxu insights < feeds.sql 