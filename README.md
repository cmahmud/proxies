# SyndProxy private pool

## Current pool

- Alive now: 1030
- Gold now: 504
- HTTP: 362 alive / 156 gold
- HTTPS: 247 alive / 90 gold
- SOCKS4: 220 alive / 141 gold
- SOCKS5: 201 alive / 117 gold

## Historical pool

- Discovered: 119845
- Ever alive: 18374
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
