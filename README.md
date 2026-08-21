# SyndProxy private pool

## Current pool

- Alive now: 938
- Gold now: 403
- HTTP: 279 alive / 94 gold
- HTTPS: 204 alive / 24 gold
- SOCKS4: 244 alive / 157 gold
- SOCKS5: 211 alive / 128 gold

## Historical pool

- Discovered: 160980
- Ever alive: 30839
- Ever gold: 1150

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
