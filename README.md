# SyndProxy private pool

## Current pool

- Alive now: 1107
- Gold now: 476
- HTTP: 389 alive / 123 gold
- HTTPS: 267 alive / 72 gold
- SOCKS4: 232 alive / 140 gold
- SOCKS5: 219 alive / 141 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16553
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
