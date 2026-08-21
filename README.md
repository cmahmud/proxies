# SyndProxy private pool

## Current pool

- Alive now: 894
- Gold now: 399
- HTTP: 280 alive / 90 gold
- HTTPS: 158 alive / 22 gold
- SOCKS4: 216 alive / 148 gold
- SOCKS5: 240 alive / 139 gold

## Historical pool

- Discovered: 155694
- Ever alive: 29231
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
