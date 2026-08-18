# SyndProxy private pool

## Current pool

- Alive now: 869
- Gold now: 259
- HTTP: 254 alive / 27 gold
- HTTPS: 157 alive / 3 gold
- SOCKS4: 234 alive / 120 gold
- SOCKS5: 224 alive / 109 gold

## Historical pool

- Discovered: 99160
- Ever alive: 12070
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
