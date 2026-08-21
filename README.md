# SyndProxy private pool

## Current pool

- Alive now: 1082
- Gold now: 400
- HTTP: 393 alive / 106 gold
- HTTPS: 232 alive / 26 gold
- SOCKS4: 222 alive / 131 gold
- SOCKS5: 235 alive / 137 gold

## Historical pool

- Discovered: 160027
- Ever alive: 30601
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
