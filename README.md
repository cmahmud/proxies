# SyndProxy private pool

## Current pool

- Alive now: 654
- Gold now: 363
- HTTP: 171 alive / 67 gold
- HTTPS: 108 alive / 22 gold
- SOCKS4: 183 alive / 129 gold
- SOCKS5: 192 alive / 145 gold

## Historical pool

- Discovered: 145580
- Ever alive: 25580
- Ever gold: 1066

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
