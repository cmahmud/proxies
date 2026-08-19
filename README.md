# SyndProxy private pool

## Current pool

- Alive now: 1020
- Gold now: 357
- HTTP: 353 alive / 71 gold
- HTTPS: 237 alive / 19 gold
- SOCKS4: 196 alive / 116 gold
- SOCKS5: 234 alive / 151 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16385
- Ever gold: 515

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
