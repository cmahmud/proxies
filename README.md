# SyndProxy private pool

## Current pool

- Alive now: 1003
- Gold now: 364
- HTTP: 344 alive / 75 gold
- HTTPS: 229 alive / 25 gold
- SOCKS4: 213 alive / 135 gold
- SOCKS5: 217 alive / 129 gold

## Historical pool

- Discovered: 165836
- Ever alive: 32360
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
