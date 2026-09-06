# SyndProxy validated proxy pool

## Current pool

- Alive now: 418
- Gold now: 348
- HTTP: 78 alive / 63 gold
- HTTPS: 30 alive / 13 gold
- SOCKS4: 148 alive / 137 gold
- SOCKS5: 162 alive / 135 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48385
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
