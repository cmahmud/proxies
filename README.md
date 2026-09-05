# SyndProxy validated proxy pool

## Current pool

- Alive now: 374
- Gold now: 289
- HTTP: 107 alive / 76 gold
- HTTPS: 34 alive / 19 gold
- SOCKS4: 74 alive / 62 gold
- SOCKS5: 159 alive / 132 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47850
- Ever gold: 1498

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
