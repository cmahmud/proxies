# SyndProxy private pool

## Current pool

- Alive now: 865
- Gold now: 373
- HTTP: 294 alive / 80 gold
- HTTPS: 164 alive / 23 gold
- SOCKS4: 184 alive / 119 gold
- SOCKS5: 223 alive / 151 gold

## Historical pool

- Discovered: 166322
- Ever alive: 32390
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
