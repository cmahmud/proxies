# SyndProxy validated proxy pool

## Current pool

- Alive now: 383
- Gold now: 293
- HTTP: 102 alive / 74 gold
- HTTPS: 59 alive / 20 gold
- SOCKS4: 70 alive / 67 gold
- SOCKS5: 152 alive / 132 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47913
- Ever gold: 1503

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
