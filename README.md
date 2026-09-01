# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 460
- HTTP: 124 alive / 87 gold
- HTTPS: 113 alive / 37 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 195 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46983
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
