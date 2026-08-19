# SyndProxy private pool

## Current pool

- Alive now: 862
- Gold now: 395
- HTTP: 262 alive / 89 gold
- HTTPS: 174 alive / 14 gold
- SOCKS4: 222 alive / 158 gold
- SOCKS5: 204 alive / 134 gold

## Historical pool

- Discovered: 119828
- Ever alive: 18238
- Ever gold: 717

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
