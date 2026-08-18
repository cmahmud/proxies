# SyndProxy private pool

## Current pool

- Alive now: 811
- Gold now: 282
- HTTP: 276 alive / 35 gold
- HTTPS: 163 alive / 10 gold
- SOCKS4: 212 alive / 139 gold
- SOCKS5: 160 alive / 98 gold

## Historical pool

- Discovered: 102917
- Ever alive: 13936
- Ever gold: 434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
