# SyndProxy private pool

## Current pool

- Alive now: 1013
- Gold now: 400
- HTTP: 291 alive / 75 gold
- HTTPS: 224 alive / 15 gold
- SOCKS4: 251 alive / 149 gold
- SOCKS5: 247 alive / 161 gold

## Historical pool

- Discovered: 131105
- Ever alive: 20536
- Ever gold: 868

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
