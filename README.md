# SyndProxy private pool

## Current pool

- Alive now: 1561
- Gold now: 611
- HTTP: 603 alive / 216 gold
- HTTPS: 498 alive / 120 gold
- SOCKS4: 222 alive / 134 gold
- SOCKS5: 238 alive / 141 gold

## Historical pool

- Discovered: 140473
- Ever alive: 23772
- Ever gold: 959

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
