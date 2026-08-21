# SyndProxy private pool

## Current pool

- Alive now: 1176
- Gold now: 438
- HTTP: 419 alive / 109 gold
- HTTPS: 271 alive / 27 gold
- SOCKS4: 221 alive / 139 gold
- SOCKS5: 265 alive / 163 gold

## Historical pool

- Discovered: 153127
- Ever alive: 28431
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
