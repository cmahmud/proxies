# SyndProxy private pool

## Current pool

- Alive now: 1216
- Gold now: 401
- HTTP: 390 alive / 90 gold
- HTTPS: 273 alive / 12 gold
- SOCKS4: 253 alive / 142 gold
- SOCKS5: 300 alive / 157 gold

## Historical pool

- Discovered: 131826
- Ever alive: 21026
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
