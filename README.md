# SyndProxy private pool

## Current pool

- Alive now: 1086
- Gold now: 361
- HTTP: 420 alive / 94 gold
- HTTPS: 256 alive / 21 gold
- SOCKS4: 185 alive / 114 gold
- SOCKS5: 225 alive / 132 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28814
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
