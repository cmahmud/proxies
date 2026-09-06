# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 391
- HTTP: 94 alive / 67 gold
- HTTPS: 34 alive / 14 gold
- SOCKS4: 164 alive / 153 gold
- SOCKS5: 183 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48236
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
