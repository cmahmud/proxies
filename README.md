# SyndProxy private pool

## Current pool

- Alive now: 855
- Gold now: 259
- HTTP: 248 alive / 28 gold
- HTTPS: 158 alive / 3 gold
- SOCKS4: 227 alive / 119 gold
- SOCKS5: 222 alive / 109 gold

## Historical pool

- Discovered: 99160
- Ever alive: 12070
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
