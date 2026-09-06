# SyndProxy validated proxy pool

## Current pool

- Alive now: 408
- Gold now: 330
- HTTP: 81 alive / 60 gold
- HTTPS: 28 alive / 10 gold
- SOCKS4: 142 alive / 135 gold
- SOCKS5: 157 alive / 125 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48383
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
