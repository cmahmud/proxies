# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 454
- HTTP: 123 alive / 83 gold
- HTTPS: 108 alive / 39 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46977
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
