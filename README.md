# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 456
- HTTP: 132 alive / 83 gold
- HTTPS: 102 alive / 37 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46993
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
