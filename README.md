# SyndProxy private pool

## Current pool

- Alive now: 950
- Gold now: 308
- HTTP: 296 alive / 38 gold
- HTTPS: 198 alive / 9 gold
- SOCKS4: 226 alive / 139 gold
- SOCKS5: 230 alive / 122 gold

## Historical pool

- Discovered: 106998
- Ever alive: 14190
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
