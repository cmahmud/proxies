# SyndProxy private pool

## Current pool

- Alive now: 1014
- Gold now: 341
- HTTP: 368 alive / 70 gold
- HTTPS: 221 alive / 15 gold
- SOCKS4: 191 alive / 111 gold
- SOCKS5: 234 alive / 145 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16384
- Ever gold: 514

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
