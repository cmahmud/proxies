# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 423
- HTTP: 84 alive / 64 gold
- HTTPS: 43 alive / 24 gold
- SOCKS4: 169 alive / 165 gold
- SOCKS5: 177 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47088
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
