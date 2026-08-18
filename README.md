# SyndProxy private pool

## Current pool

- Alive now: 837
- Gold now: 267
- HTTP: 213 alive / 28 gold
- HTTPS: 159 alive / 4 gold
- SOCKS4: 220 alive / 121 gold
- SOCKS5: 245 alive / 114 gold

## Historical pool

- Discovered: 99165
- Ever alive: 12139
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
