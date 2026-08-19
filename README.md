# SyndProxy private pool

## Current pool

- Alive now: 1070
- Gold now: 498
- HTTP: 388 alive / 168 gold
- HTTPS: 244 alive / 47 gold
- SOCKS4: 225 alive / 139 gold
- SOCKS5: 213 alive / 144 gold

## Historical pool

- Discovered: 124833
- Ever alive: 19167
- Ever gold: 731

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
