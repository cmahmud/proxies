# SyndProxy private pool

## Current pool

- Alive now: 1056
- Gold now: 417
- HTTP: 352 alive / 102 gold
- HTTPS: 257 alive / 35 gold
- SOCKS4: 213 alive / 139 gold
- SOCKS5: 234 alive / 141 gold

## Historical pool

- Discovered: 160257
- Ever alive: 30693
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
