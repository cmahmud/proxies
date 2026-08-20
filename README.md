# SyndProxy private pool

## Current pool

- Alive now: 1608
- Gold now: 611
- HTTP: 566 alive / 211 gold
- HTTPS: 472 alive / 117 gold
- SOCKS4: 225 alive / 147 gold
- SOCKS5: 345 alive / 136 gold

## Historical pool

- Discovered: 140465
- Ever alive: 23686
- Ever gold: 954

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
