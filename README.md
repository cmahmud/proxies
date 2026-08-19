# SyndProxy private pool

## Current pool

- Alive now: 1013
- Gold now: 541
- HTTP: 327 alive / 160 gold
- HTTPS: 256 alive / 89 gold
- SOCKS4: 217 alive / 155 gold
- SOCKS5: 213 alive / 137 gold

## Historical pool

- Discovered: 119845
- Ever alive: 18403
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
