# SyndProxy private pool

## Current pool

- Alive now: 1084
- Gold now: 285
- HTTP: 388 alive / 30 gold
- HTTPS: 216 alive / 4 gold
- SOCKS4: 243 alive / 137 gold
- SOCKS5: 237 alive / 114 gold

## Historical pool

- Discovered: 100097
- Ever alive: 12661
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
