# SyndProxy private pool

## Current pool

- Alive now: 1025
- Gold now: 404
- HTTP: 341 alive / 109 gold
- HTTPS: 261 alive / 29 gold
- SOCKS4: 202 alive / 144 gold
- SOCKS5: 221 alive / 122 gold

## Historical pool

- Discovered: 153184
- Ever alive: 28489
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
