# SyndProxy private pool

## Current pool

- Alive now: 1059
- Gold now: 363
- HTTP: 405 alive / 91 gold
- HTTPS: 244 alive / 22 gold
- SOCKS4: 188 alive / 117 gold
- SOCKS5: 222 alive / 133 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28814
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
