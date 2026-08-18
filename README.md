# SyndProxy private pool

## Current pool

- Alive now: 830
- Gold now: 282
- HTTP: 279 alive / 35 gold
- HTTPS: 182 alive / 9 gold
- SOCKS4: 207 alive / 139 gold
- SOCKS5: 162 alive / 99 gold

## Historical pool

- Discovered: 102917
- Ever alive: 13958
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
