# SyndProxy private pool

## Current pool

- Alive now: 1327
- Gold now: 428
- HTTP: 463 alive / 94 gold
- HTTPS: 301 alive / 24 gold
- SOCKS4: 245 alive / 148 gold
- SOCKS5: 318 alive / 162 gold

## Historical pool

- Discovered: 136218
- Ever alive: 22445
- Ever gold: 900

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
