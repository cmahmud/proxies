# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 369
- HTTP: 96 alive / 53 gold
- HTTPS: 39 alive / 10 gold
- SOCKS4: 168 alive / 152 gold
- SOCKS5: 176 alive / 154 gold

## Historical pool

- Discovered: 174122
- Ever alive: 33052
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
