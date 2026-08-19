# SyndProxy private pool

## Current pool

- Alive now: 1094
- Gold now: 336
- HTTP: 402 alive / 64 gold
- HTTPS: 273 alive / 17 gold
- SOCKS4: 189 alive / 113 gold
- SOCKS5: 230 alive / 142 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16346
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
