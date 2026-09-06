# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 388
- HTTP: 94 alive / 71 gold
- HTTPS: 39 alive / 14 gold
- SOCKS4: 167 alive / 150 gold
- SOCKS5: 173 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48208
- Ever gold: 1524

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
