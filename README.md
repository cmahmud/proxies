# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 456
- HTTP: 131 alive / 84 gold
- HTTPS: 102 alive / 36 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46991
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
