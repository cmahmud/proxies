# SyndProxy private pool

## Current pool

- Alive now: 1027
- Gold now: 408
- HTTP: 336 alive / 94 gold
- HTTPS: 205 alive / 26 gold
- SOCKS4: 220 alive / 139 gold
- SOCKS5: 266 alive / 149 gold

## Historical pool

- Discovered: 154717
- Ever alive: 29023
- Ever gold: 1119

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
