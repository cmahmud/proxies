# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 485
- HTTP: 140 alive / 102 gold
- HTTPS: 121 alive / 44 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 205 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44932
- Ever gold: 1419

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
