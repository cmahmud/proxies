# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 388
- HTTP: 93 alive / 61 gold
- HTTPS: 42 alive / 15 gold
- SOCKS4: 179 alive / 156 gold
- SOCKS5: 178 alive / 156 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48157
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
