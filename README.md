# SyndProxy private pool

## Current pool

- Alive now: 1027
- Gold now: 399
- HTTP: 331 alive / 85 gold
- HTTPS: 202 alive / 20 gold
- SOCKS4: 240 alive / 149 gold
- SOCKS5: 254 alive / 145 gold

## Historical pool

- Discovered: 158238
- Ever alive: 29988
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
