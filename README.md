# SyndProxy private pool

## Current pool

- Alive now: 1096
- Gold now: 461
- HTTP: 425 alive / 119 gold
- HTTPS: 252 alive / 74 gold
- SOCKS4: 208 alive / 139 gold
- SOCKS5: 211 alive / 129 gold

## Historical pool

- Discovered: 113546
- Ever alive: 16629
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
