# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 419
- HTTP: 87 alive / 62 gold
- HTTPS: 44 alive / 24 gold
- SOCKS4: 170 alive / 165 gold
- SOCKS5: 177 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47088
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
