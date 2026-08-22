# SyndProxy private pool

## Current pool

- Alive now: 944
- Gold now: 404
- HTTP: 292 alive / 94 gold
- HTTPS: 168 alive / 19 gold
- SOCKS4: 223 alive / 133 gold
- SOCKS5: 261 alive / 158 gold

## Historical pool

- Discovered: 166610
- Ever alive: 32433
- Ever gold: 1182

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
