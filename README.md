# SyndProxy private pool

## Current pool

- Alive now: 1563
- Gold now: 614
- HTTP: 601 alive / 214 gold
- HTTPS: 497 alive / 120 gold
- SOCKS4: 227 alive / 135 gold
- SOCKS5: 238 alive / 145 gold

## Historical pool

- Discovered: 140473
- Ever alive: 23766
- Ever gold: 957

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
