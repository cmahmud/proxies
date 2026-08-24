# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 431
- HTTP: 129 alive / 78 gold
- HTTPS: 89 alive / 21 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 189 alive / 170 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33916
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
