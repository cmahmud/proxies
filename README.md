# SyndProxy private pool

## Current pool

- Alive now: 960
- Gold now: 428
- HTTP: 293 alive / 107 gold
- HTTPS: 196 alive / 32 gold
- SOCKS4: 232 alive / 150 gold
- SOCKS5: 239 alive / 139 gold

## Historical pool

- Discovered: 160276
- Ever alive: 30752
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
