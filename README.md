# SyndProxy private pool

## Current pool

- Alive now: 777
- Gold now: 382
- HTTP: 209 alive / 76 gold
- HTTPS: 136 alive / 23 gold
- SOCKS4: 199 alive / 136 gold
- SOCKS5: 233 alive / 147 gold

## Historical pool

- Discovered: 147687
- Ever alive: 25961
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
