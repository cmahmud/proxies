# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 463
- HTTP: 139 alive / 93 gold
- HTTPS: 113 alive / 36 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 208 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44858
- Ever gold: 1417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
