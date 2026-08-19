# SyndProxy private pool

## Current pool

- Alive now: 1049
- Gold now: 401
- HTTP: 336 alive / 75 gold
- HTTPS: 204 alive / 15 gold
- SOCKS4: 258 alive / 149 gold
- SOCKS5: 251 alive / 162 gold

## Historical pool

- Discovered: 131104
- Ever alive: 20536
- Ever gold: 868

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
