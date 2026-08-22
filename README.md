# SyndProxy private pool

## Current pool

- Alive now: 914
- Gold now: 328
- HTTP: 311 alive / 85 gold
- HTTPS: 246 alive / 29 gold
- SOCKS4: 177 alive / 127 gold
- SOCKS5: 180 alive / 87 gold

## Historical pool

- Discovered: 166948
- Ever alive: 32487
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
