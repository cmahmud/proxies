# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 447
- HTTP: 96 alive / 77 gold
- HTTPS: 100 alive / 31 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 192 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47351
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
