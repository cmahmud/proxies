# SyndProxy private pool

## Current pool

- Alive now: 1207
- Gold now: 452
- HTTP: 471 alive / 119 gold
- HTTPS: 273 alive / 73 gold
- SOCKS4: 234 alive / 134 gold
- SOCKS5: 229 alive / 126 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16732
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
