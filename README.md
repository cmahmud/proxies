# SyndProxy private pool

## Current pool

- Alive now: 975
- Gold now: 320
- HTTP: 309 alive / 38 gold
- HTTPS: 187 alive / 10 gold
- SOCKS4: 238 alive / 139 gold
- SOCKS5: 241 alive / 133 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14242
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
