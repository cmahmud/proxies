# SyndProxy private pool

## Current pool

- Alive now: 978
- Gold now: 340
- HTTP: 333 alive / 69 gold
- HTTPS: 225 alive / 15 gold
- SOCKS4: 188 alive / 111 gold
- SOCKS5: 232 alive / 145 gold

## Historical pool

- Discovered: 113527
- Ever alive: 16383
- Ever gold: 514

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
