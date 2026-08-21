# SyndProxy private pool

## Current pool

- Alive now: 1132
- Gold now: 389
- HTTP: 400 alive / 101 gold
- HTTPS: 254 alive / 25 gold
- SOCKS4: 218 alive / 124 gold
- SOCKS5: 260 alive / 139 gold

## Historical pool

- Discovered: 152217
- Ever alive: 27967
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
