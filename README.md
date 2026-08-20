# SyndProxy private pool

## Current pool

- Alive now: 717
- Gold now: 383
- HTTP: 204 alive / 70 gold
- HTTPS: 104 alive / 19 gold
- SOCKS4: 195 alive / 138 gold
- SOCKS5: 214 alive / 156 gold

## Historical pool

- Discovered: 147178
- Ever alive: 25813
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
