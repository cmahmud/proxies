# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 431
- HTTP: 97 alive / 72 gold
- HTTPS: 114 alive / 31 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 182 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47301
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
