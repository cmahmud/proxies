# SyndProxy private pool

## Current pool

- Alive now: 1021
- Gold now: 395
- HTTP: 297 alive / 97 gold
- HTTPS: 248 alive / 26 gold
- SOCKS4: 236 alive / 133 gold
- SOCKS5: 240 alive / 139 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25109
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
