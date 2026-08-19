# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 348
- HTTP: 348 alive / 72 gold
- HTTPS: 231 alive / 16 gold
- SOCKS4: 202 alive / 113 gold
- SOCKS5: 230 alive / 147 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16385
- Ever gold: 515

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
