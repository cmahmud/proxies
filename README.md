# SyndProxy private pool

## Current pool

- Alive now: 977
- Gold now: 401
- HTTP: 309 alive / 93 gold
- HTTPS: 224 alive / 36 gold
- SOCKS4: 212 alive / 139 gold
- SOCKS5: 232 alive / 133 gold

## Historical pool

- Discovered: 161987
- Ever alive: 31290
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
