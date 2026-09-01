# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 418
- HTTP: 84 alive / 61 gold
- HTTPS: 45 alive / 23 gold
- SOCKS4: 170 alive / 165 gold
- SOCKS5: 177 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47088
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
