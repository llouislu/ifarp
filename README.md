# ifarp: Ipipnet Free dAtabase RiPper
ipip.net 免费 IP 数据库转 csv 工具

## 依赖

1. Python 3
2. Python 3 的 `csv` `math` **`ipdb`** `re` `struct` `sys` 模块
3. 一份 ipip.net 的数据库（[下载](https://www.ipip.net/free_download/)）

## 用法

```
ifarp.py <数据库文件.dat> <输出.csv>
```

## 输出 csv 格式

```
整数型开始ip,整数型结束ip,"地区名称"
```

例如：
```
16777216,16777472,"APNIC APNIC"
```

## MySQL 数据库导入与查询

### 建表

```
CREATE TABLE `iploc` (
    `startIpNum` INT(10) UNSIGNED NULL,
    `endIpNum` INT(10) UNSIGNED NULL,
    `loc` VARCHAR(64) NULL
)  ENGINE=INNODB DEFAULT CHARACTER SET=UTF8;
```

### 查询

```
set @ip = '127.0.0.1';
SELECT
    @ip, loc
FROM
    `iploc`
WHERE
    INET_ATON(@ip) <= endIpNum
LIMIT 1;

# 输出
# @ip, loc
# 127.0.0.1, 局域网 局域网
```