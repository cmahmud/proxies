# SyndProxy private pool

## Current pool

- Alive now: 828
- Gold now: 422
- HTTP: 215 alive / 80 gold
- HTTPS: 156 alive / 30 gold
- SOCKS4: 233 alive / 152 gold
- SOCKS5: 224 alive / 160 gold

## Historical pool

- Discovered: 151059
- Ever alive: 27311
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
