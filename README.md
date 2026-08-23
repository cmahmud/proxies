# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 393
- HTTP: 112 alive / 67 gold
- HTTPS: 45 alive / 14 gold
- SOCKS4: 159 alive / 153 gold
- SOCKS5: 185 alive / 159 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33180
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
