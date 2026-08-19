# SyndProxy private pool

## Current pool

- Alive now: 1039
- Gold now: 395
- HTTP: 337 alive / 73 gold
- HTTPS: 203 alive / 13 gold
- SOCKS4: 265 alive / 151 gold
- SOCKS5: 234 alive / 158 gold

## Historical pool

- Discovered: 129331
- Ever alive: 20496
- Ever gold: 866

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
