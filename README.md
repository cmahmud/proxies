# SyndProxy private pool

## Current pool

- Alive now: 1022
- Gold now: 575
- HTTP: 311 alive / 190 gold
- HTTPS: 233 alive / 98 gold
- SOCKS4: 218 alive / 139 gold
- SOCKS5: 260 alive / 148 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23239
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
