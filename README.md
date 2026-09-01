# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 428
- HTTP: 108 alive / 74 gold
- HTTPS: 72 alive / 27 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 180 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47051
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
