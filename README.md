# SyndProxy private pool

## Current pool

- Alive now: 1585
- Gold now: 607
- HTTP: 598 alive / 206 gold
- HTTPS: 416 alive / 115 gold
- SOCKS4: 229 alive / 149 gold
- SOCKS5: 342 alive / 137 gold

## Historical pool

- Discovered: 140465
- Ever alive: 23657
- Ever gold: 954

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
