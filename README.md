# SyndProxy validated proxy pool

## Current pool

- Alive now: 418
- Gold now: 313
- HTTP: 80 alive / 54 gold
- HTTPS: 43 alive / 7 gold
- SOCKS4: 148 alive / 132 gold
- SOCKS5: 147 alive / 120 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48367
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
