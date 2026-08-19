# SyndProxy private pool

## Current pool

- Alive now: 1245
- Gold now: 413
- HTTP: 414 alive / 88 gold
- HTTPS: 305 alive / 22 gold
- SOCKS4: 240 alive / 142 gold
- SOCKS5: 286 alive / 161 gold

## Historical pool

- Discovered: 136183
- Ever alive: 22301
- Ever gold: 895

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
