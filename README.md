# SyndProxy private pool

## Current pool

- Alive now: 1022
- Gold now: 422
- HTTP: 342 alive / 91 gold
- HTTPS: 222 alive / 23 gold
- SOCKS4: 222 alive / 158 gold
- SOCKS5: 236 alive / 150 gold

## Historical pool

- Discovered: 158252
- Ever alive: 30058
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
