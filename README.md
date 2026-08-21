# SyndProxy private pool

## Current pool

- Alive now: 1033
- Gold now: 361
- HTTP: 386 alive / 94 gold
- HTTPS: 249 alive / 21 gold
- SOCKS4: 178 alive / 114 gold
- SOCKS5: 220 alive / 132 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28814
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
