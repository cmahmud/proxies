# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 447
- HTTP: 101 alive / 77 gold
- HTTPS: 99 alive / 31 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 194 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47391
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
