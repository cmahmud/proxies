# SyndProxy private pool

## Current pool

- Alive now: 992
- Gold now: 413
- HTTP: 314 alive / 85 gold
- HTTPS: 218 alive / 27 gold
- SOCKS4: 220 alive / 143 gold
- SOCKS5: 240 alive / 158 gold

## Historical pool

- Discovered: 159211
- Ever alive: 30190
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
