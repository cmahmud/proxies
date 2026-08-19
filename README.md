# SyndProxy private pool

## Current pool

- Alive now: 1146
- Gold now: 512
- HTTP: 408 alive / 122 gold
- HTTPS: 236 alive / 74 gold
- SOCKS4: 233 alive / 155 gold
- SOCKS5: 269 alive / 161 gold

## Historical pool

- Discovered: 114411
- Ever alive: 16988
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
