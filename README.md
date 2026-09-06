# SyndProxy validated proxy pool

## Current pool

- Alive now: 423
- Gold now: 331
- HTTP: 81 alive / 61 gold
- HTTPS: 34 alive / 9 gold
- SOCKS4: 152 alive / 137 gold
- SOCKS5: 156 alive / 124 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48380
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
