# SyndProxy private pool

## Current pool

- Alive now: 1376
- Gold now: 556
- HTTP: 446 alive / 185 gold
- HTTPS: 359 alive / 90 gold
- SOCKS4: 240 alive / 149 gold
- SOCKS5: 331 alive / 132 gold

## Historical pool

- Discovered: 140465
- Ever alive: 23616
- Ever gold: 924

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
