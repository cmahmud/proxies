# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 441
- HTTP: 101 alive / 71 gold
- HTTPS: 104 alive / 31 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 189 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47452
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
