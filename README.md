# SyndProxy private pool

## Current pool

- Alive now: 1052
- Gold now: 275
- HTTP: 437 alive / 31 gold
- HTTPS: 169 alive / 5 gold
- SOCKS4: 234 alive / 132 gold
- SOCKS5: 212 alive / 107 gold

## Historical pool

- Discovered: 99059
- Ever alive: 11373
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
