# SyndProxy validated proxy pool

## Current pool

- Alive now: 660
- Gold now: 468
- HTTP: 138 alive / 94 gold
- HTTPS: 134 alive / 35 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 211 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46442
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
