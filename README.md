# SyndProxy private pool

## Current pool

- Alive now: 1042
- Gold now: 413
- HTTP: 348 alive / 93 gold
- HTTPS: 215 alive / 28 gold
- SOCKS4: 224 alive / 133 gold
- SOCKS5: 255 alive / 159 gold

## Historical pool

- Discovered: 166609
- Ever alive: 32425
- Ever gold: 1180

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
