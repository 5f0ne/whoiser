# Description

whois information for given IP addresses

# Installation

`pip install whoiser`

# Usage

**From command line:**

`python -m whoiser --path PATH`

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--path | -p | String | - | Path to list of IPs |


# Example

`python -m whoiser -p addr.txt > result.txt`

```
################################################################################

whoiser by 5f0
whois information for given IP addresses

Current working directory: path/to/whoiser

Datetime: 01/01/1970 10:11:12

################################################################################

+----------------+------------------+-------------------------------+----------------------+-----------------------+
|     Query      |      CIDR        |             Range             |     Network Name     |      Contact Name     |
+----------------+------------------+-------------------------------+----------------------+-----------------------+
|  20.81.111.85  | 20.33.0.0/16 (+) |   20.33.0.0 - 20.128.255.255  |         MSFT         | Microsoft Corporation |
| 74.125.225.229 | 74.125.0.0/16    |  74.125.0.0 - 74.125.255.255  |         GOOGLE       |       Google LLC      |
| 185.60.216.35  | 185.60.216.0/22  | 185.60.216.0 - 185.60.219.255 | IE-FACEBOOK-20140612 |        meta-mnt       |
+----------------+------------------+-------------------------------+----------------------+-----------------------+

################################################################################

Execution Time: 46.01186 sec

```

# License

MIT