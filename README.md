# SyndProxy validated proxy pool

## Current pool

- Alive now: 600
- Gold now: 457
- HTTP: 132 alive / 84 gold
- HTTPS: 103 alive / 37 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46993
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
