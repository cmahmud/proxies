# SyndProxy private pool

## Current pool

- Alive now: 597
- Gold now: 227
- HTTP: 180 alive / 38 gold
- HTTPS: 89 alive / 10 gold
- SOCKS4: 158 alive / 102 gold
- SOCKS5: 170 alive / 77 gold

## Historical pool

- Discovered: 86651
- Ever alive: 5727
- Ever gold: 294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
