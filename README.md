# SyndProxy private pool

## Current pool

- Alive now: 1260
- Gold now: 413
- HTTP: 432 alive / 90 gold
- HTTPS: 291 alive / 21 gold
- SOCKS4: 242 alive / 141 gold
- SOCKS5: 295 alive / 161 gold

## Historical pool

- Discovered: 136183
- Ever alive: 22239
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
