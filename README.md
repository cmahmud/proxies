# SyndProxy private pool

## Current pool

- Alive now: 1200
- Gold now: 449
- HTTP: 435 alive / 106 gold
- HTTPS: 292 alive / 29 gold
- SOCKS4: 204 alive / 153 gold
- SOCKS5: 269 alive / 161 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28575
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
