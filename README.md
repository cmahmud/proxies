# SyndProxy private pool

## Current pool

- Alive now: 810
- Gold now: 413
- HTTP: 209 alive / 81 gold
- HTTPS: 140 alive / 24 gold
- SOCKS4: 207 alive / 143 gold
- SOCKS5: 254 alive / 165 gold

## Historical pool

- Discovered: 155796
- Ever alive: 29344
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
