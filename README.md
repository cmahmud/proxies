# SyndProxy private pool

## Current pool

- Alive now: 955
- Gold now: 422
- HTTP: 277 alive / 91 gold
- HTTPS: 219 alive / 28 gold
- SOCKS4: 208 alive / 144 gold
- SOCKS5: 251 alive / 159 gold

## Historical pool

- Discovered: 162749
- Ever alive: 31543
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
