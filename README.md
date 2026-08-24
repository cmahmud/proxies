# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 432
- HTTP: 103 alive / 76 gold
- HTTPS: 70 alive / 24 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 204 alive / 170 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34089
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
