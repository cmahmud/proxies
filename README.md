# SyndProxy private pool

## Current pool

- Alive now: 1080
- Gold now: 367
- HTTP: 380 alive / 82 gold
- HTTPS: 295 alive / 22 gold
- SOCKS4: 182 alive / 115 gold
- SOCKS5: 223 alive / 148 gold

## Historical pool

- Discovered: 158226
- Ever alive: 29885
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
