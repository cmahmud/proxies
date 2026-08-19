# SyndProxy private pool

## Current pool

- Alive now: 1114
- Gold now: 531
- HTTP: 404 alive / 157 gold
- HTTPS: 277 alive / 91 gold
- SOCKS4: 200 alive / 139 gold
- SOCKS5: 233 alive / 144 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18617
- Ever gold: 721

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
