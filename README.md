# SyndProxy validated proxy pool

## Current pool

- Alive now: 591
- Gold now: 455
- HTTP: 124 alive / 83 gold
- HTTPS: 106 alive / 37 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 189 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46995
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
