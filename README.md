# SyndProxy private pool

## Current pool

- Alive now: 752
- Gold now: 268
- HTTP: 205 alive / 23 gold
- HTTPS: 135 alive / 2 gold
- SOCKS4: 218 alive / 136 gold
- SOCKS5: 194 alive / 107 gold

## Historical pool

- Discovered: 99093
- Ever alive: 11473
- Ever gold: 385

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
