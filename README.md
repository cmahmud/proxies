# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 394
- HTTP: 94 alive / 70 gold
- HTTPS: 33 alive / 14 gold
- SOCKS4: 159 alive / 153 gold
- SOCKS5: 185 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48236
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
