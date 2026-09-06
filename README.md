# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 391
- HTTP: 96 alive / 70 gold
- HTTPS: 33 alive / 13 gold
- SOCKS4: 165 alive / 153 gold
- SOCKS5: 183 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48236
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
