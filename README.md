# SyndProxy private pool

## Current pool

- Alive now: 1083
- Gold now: 401
- HTTP: 367 alive / 100 gold
- HTTPS: 268 alive / 28 gold
- SOCKS4: 189 alive / 121 gold
- SOCKS5: 259 alive / 152 gold

## Historical pool

- Discovered: 152758
- Ever alive: 28341
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
