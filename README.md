# SyndProxy private pool

## Current pool

- Alive now: 1203
- Gold now: 443
- HTTP: 439 alive / 101 gold
- HTTPS: 298 alive / 31 gold
- SOCKS4: 203 alive / 139 gold
- SOCKS5: 263 alive / 172 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28721
- Ever gold: 1113

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
