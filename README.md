# SyndProxy private pool

## Current pool

- Alive now: 1071
- Gold now: 379
- HTTP: 388 alive / 85 gold
- HTTPS: 274 alive / 26 gold
- SOCKS4: 161 alive / 104 gold
- SOCKS5: 248 alive / 164 gold

## Historical pool

- Discovered: 166635
- Ever alive: 32463
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
