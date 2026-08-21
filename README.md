# SyndProxy private pool

## Current pool

- Alive now: 900
- Gold now: 396
- HTTP: 276 alive / 87 gold
- HTTPS: 159 alive / 22 gold
- SOCKS4: 221 alive / 148 gold
- SOCKS5: 244 alive / 139 gold

## Historical pool

- Discovered: 155694
- Ever alive: 29228
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
