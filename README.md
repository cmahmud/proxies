# SyndProxy private pool

## Current pool

- Alive now: 1507
- Gold now: 611
- HTTP: 563 alive / 213 gold
- HTTPS: 484 alive / 112 gold
- SOCKS4: 233 alive / 150 gold
- SOCKS5: 227 alive / 136 gold

## Historical pool

- Discovered: 140473
- Ever alive: 23752
- Ever gold: 956

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
