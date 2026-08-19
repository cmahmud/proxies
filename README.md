# SyndProxy private pool

## Current pool

- Alive now: 1261
- Gold now: 413
- HTTP: 434 alive / 90 gold
- HTTPS: 287 alive / 21 gold
- SOCKS4: 239 alive / 140 gold
- SOCKS5: 301 alive / 162 gold

## Historical pool

- Discovered: 136183
- Ever alive: 22243
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
