# SyndProxy private pool

## Current pool

- Alive now: 746
- Gold now: 268
- HTTP: 207 alive / 23 gold
- HTTPS: 126 alive / 2 gold
- SOCKS4: 221 alive / 136 gold
- SOCKS5: 192 alive / 107 gold

## Historical pool

- Discovered: 99079
- Ever alive: 11472
- Ever gold: 385

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
