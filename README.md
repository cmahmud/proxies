# SyndProxy private pool

## Current pool

- Alive now: 1075
- Gold now: 432
- HTTP: 362 alive / 102 gold
- HTTPS: 236 alive / 29 gold
- SOCKS4: 206 alive / 141 gold
- SOCKS5: 271 alive / 160 gold

## Historical pool

- Discovered: 153731
- Ever alive: 28661
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
