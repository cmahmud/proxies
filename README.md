# SyndProxy private pool

## Current pool

- Alive now: 1021
- Gold now: 346
- HTTP: 353 alive / 69 gold
- HTTPS: 258 alive / 19 gold
- SOCKS4: 178 alive / 114 gold
- SOCKS5: 232 alive / 144 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16371
- Ever gold: 514

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
