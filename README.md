# SyndProxy private pool

## Current pool

- Alive now: 1060
- Gold now: 372
- HTTP: 369 alive / 82 gold
- HTTPS: 269 alive / 21 gold
- SOCKS4: 185 alive / 117 gold
- SOCKS5: 237 alive / 152 gold

## Historical pool

- Discovered: 158229
- Ever alive: 29900
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
