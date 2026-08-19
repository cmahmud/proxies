# SyndProxy private pool

## Current pool

- Alive now: 1061
- Gold now: 348
- HTTP: 368 alive / 69 gold
- HTTPS: 265 alive / 19 gold
- SOCKS4: 192 alive / 114 gold
- SOCKS5: 236 alive / 146 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16363
- Ever gold: 514

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
