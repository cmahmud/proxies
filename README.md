# SyndProxy private pool

## Current pool

- Alive now: 1211
- Gold now: 422
- HTTP: 400 alive / 91 gold
- HTTPS: 276 alive / 22 gold
- SOCKS4: 235 alive / 141 gold
- SOCKS5: 300 alive / 168 gold

## Historical pool

- Discovered: 136183
- Ever alive: 22243
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
