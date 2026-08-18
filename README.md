# SyndProxy private pool

## Current pool

- Alive now: 950
- Gold now: 348
- HTTP: 298 alive / 54 gold
- HTTPS: 183 alive / 14 gold
- SOCKS4: 232 alive / 139 gold
- SOCKS5: 237 alive / 141 gold

## Historical pool

- Discovered: 107067
- Ever alive: 14692
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
