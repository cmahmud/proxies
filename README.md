# SyndProxy private pool

## Current pool

- Alive now: 1096
- Gold now: 538
- HTTP: 362 alive / 162 gold
- HTTPS: 281 alive / 89 gold
- SOCKS4: 216 alive / 139 gold
- SOCKS5: 237 alive / 148 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18556
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
