# SyndProxy private pool

## Current pool

- Alive now: 880
- Gold now: 405
- HTTP: 264 alive / 82 gold
- HTTPS: 168 alive / 29 gold
- SOCKS4: 208 alive / 131 gold
- SOCKS5: 240 alive / 163 gold

## Historical pool

- Discovered: 162746
- Ever alive: 31503
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
