# SyndProxy private pool

## Current pool

- Alive now: 1176
- Gold now: 391
- HTTP: 391 alive / 89 gold
- HTTPS: 269 alive / 20 gold
- SOCKS4: 215 alive / 132 gold
- SOCKS5: 301 alive / 150 gold

## Historical pool

- Discovered: 134558
- Ever alive: 22146
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
