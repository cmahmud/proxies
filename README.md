# SyndProxy private pool

## Current pool

- Alive now: 1038
- Gold now: 394
- HTTP: 309 alive / 95 gold
- HTTPS: 254 alive / 26 gold
- SOCKS4: 235 alive / 134 gold
- SOCKS5: 240 alive / 139 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25109
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
