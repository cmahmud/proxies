# SyndProxy private pool

## Current pool

- Alive now: 880
- Gold now: 404
- HTTP: 248 alive / 76 gold
- HTTPS: 203 alive / 19 gold
- SOCKS4: 215 alive / 156 gold
- SOCKS5: 214 alive / 153 gold

## Historical pool

- Discovered: 149509
- Ever alive: 26818
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
