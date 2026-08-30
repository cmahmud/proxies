# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 472
- HTTP: 134 alive / 96 gold
- HTTPS: 121 alive / 38 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 198 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44886
- Ever gold: 1417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
