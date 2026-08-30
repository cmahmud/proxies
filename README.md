# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 432
- HTTP: 127 alive / 89 gold
- HTTPS: 78 alive / 34 gold
- SOCKS4: 162 alive / 151 gold
- SOCKS5: 178 alive / 158 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44076
- Ever gold: 1396

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
