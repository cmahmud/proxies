# SyndProxy validated proxy pool

## Current pool

- Alive now: 383
- Gold now: 297
- HTTP: 101 alive / 75 gold
- HTTPS: 59 alive / 22 gold
- SOCKS4: 71 alive / 67 gold
- SOCKS5: 152 alive / 133 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47913
- Ever gold: 1503

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
