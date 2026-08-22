# SyndProxy private pool

## Current pool

- Alive now: 923
- Gold now: 367
- HTTP: 296 alive / 81 gold
- HTTPS: 193 alive / 24 gold
- SOCKS4: 208 alive / 124 gold
- SOCKS5: 226 alive / 138 gold

## Historical pool

- Discovered: 165812
- Ever alive: 32319
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
