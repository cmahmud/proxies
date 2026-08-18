# SyndProxy private pool

## Current pool

- Alive now: 709
- Gold now: 260
- HTTP: 236 alive / 30 gold
- HTTPS: 85 alive / 8 gold
- SOCKS4: 192 alive / 132 gold
- SOCKS5: 196 alive / 90 gold

## Historical pool

- Discovered: 91741
- Ever alive: 9191
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
