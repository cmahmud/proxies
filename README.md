# SyndProxy private pool

## Current pool

- Alive now: 1093
- Gold now: 341
- HTTP: 394 alive / 69 gold
- HTTPS: 271 alive / 17 gold
- SOCKS4: 192 alive / 109 gold
- SOCKS5: 236 alive / 146 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16341
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
