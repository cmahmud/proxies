# SyndProxy private pool

## Current pool

- Alive now: 1075
- Gold now: 402
- HTTP: 309 alive / 89 gold
- HTTPS: 218 alive / 14 gold
- SOCKS4: 256 alive / 148 gold
- SOCKS5: 292 alive / 151 gold

## Historical pool

- Discovered: 131828
- Ever alive: 21081
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
