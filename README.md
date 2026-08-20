# SyndProxy private pool

## Current pool

- Alive now: 1585
- Gold now: 613
- HTTP: 608 alive / 216 gold
- HTTPS: 509 alive / 120 gold
- SOCKS4: 227 alive / 135 gold
- SOCKS5: 241 alive / 142 gold

## Historical pool

- Discovered: 140473
- Ever alive: 23771
- Ever gold: 959

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
