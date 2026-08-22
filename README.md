# SyndProxy private pool

## Current pool

- Alive now: 1052
- Gold now: 401
- HTTP: 360 alive / 88 gold
- HTTPS: 257 alive / 27 gold
- SOCKS4: 189 alive / 116 gold
- SOCKS5: 246 alive / 170 gold

## Historical pool

- Discovered: 166621
- Ever alive: 32451
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
