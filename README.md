# SyndProxy private pool

## Current pool

- Alive now: 1498
- Gold now: 613
- HTTP: 563 alive / 214 gold
- HTTPS: 483 alive / 114 gold
- SOCKS4: 227 alive / 150 gold
- SOCKS5: 225 alive / 135 gold

## Historical pool

- Discovered: 140473
- Ever alive: 23752
- Ever gold: 956

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
