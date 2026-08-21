# SyndProxy private pool

## Current pool

- Alive now: 1165
- Gold now: 438
- HTTP: 411 alive / 107 gold
- HTTPS: 293 alive / 30 gold
- SOCKS4: 205 alive / 153 gold
- SOCKS5: 256 alive / 148 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28632
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
