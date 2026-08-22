# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 422
- HTTP: 343 alive / 93 gold
- HTTPS: 236 alive / 26 gold
- SOCKS4: 206 alive / 147 gold
- SOCKS5: 246 alive / 156 gold

## Historical pool

- Discovered: 162751
- Ever alive: 31550
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
