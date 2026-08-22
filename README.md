# SyndProxy private pool

## Current pool

- Alive now: 865
- Gold now: 409
- HTTP: 291 alive / 89 gold
- HTTPS: 145 alive / 24 gold
- SOCKS4: 213 alive / 148 gold
- SOCKS5: 216 alive / 148 gold

## Historical pool

- Discovered: 166322
- Ever alive: 32389
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
