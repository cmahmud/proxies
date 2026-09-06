# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 388
- HTTP: 101 alive / 72 gold
- HTTPS: 43 alive / 15 gold
- SOCKS4: 162 alive / 150 gold
- SOCKS5: 170 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48206
- Ever gold: 1524

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
