# SyndProxy private pool

## Current pool

- Alive now: 1226
- Gold now: 413
- HTTP: 412 alive / 88 gold
- HTTPS: 287 alive / 22 gold
- SOCKS4: 242 alive / 141 gold
- SOCKS5: 285 alive / 162 gold

## Historical pool

- Discovered: 136183
- Ever alive: 22290
- Ever gold: 895

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
