# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 396
- HTTP: 97 alive / 74 gold
- HTTPS: 35 alive / 15 gold
- SOCKS4: 162 alive / 153 gold
- SOCKS5: 180 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48235
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
