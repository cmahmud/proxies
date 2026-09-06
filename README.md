# SyndProxy validated proxy pool

## Current pool

- Alive now: 421
- Gold now: 349
- HTTP: 83 alive / 66 gold
- HTTPS: 30 alive / 13 gold
- SOCKS4: 151 alive / 139 gold
- SOCKS5: 157 alive / 131 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48381
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
