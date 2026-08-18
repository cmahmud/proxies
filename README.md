# SyndProxy private pool

## Current pool

- Alive now: 671
- Gold now: 237
- HTTP: 185 alive / 37 gold
- HTTPS: 87 alive / 7 gold
- SOCKS4: 204 alive / 124 gold
- SOCKS5: 195 alive / 69 gold

## Historical pool

- Discovered: 94326
- Ever alive: 9377
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
