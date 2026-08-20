# SyndProxy private pool

## Current pool

- Alive now: 739
- Gold now: 371
- HTTP: 200 alive / 79 gold
- HTTPS: 114 alive / 22 gold
- SOCKS4: 199 alive / 135 gold
- SOCKS5: 226 alive / 135 gold

## Historical pool

- Discovered: 147687
- Ever alive: 25954
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
