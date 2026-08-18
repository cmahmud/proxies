# SyndProxy private pool

## Current pool

- Alive now: 977
- Gold now: 256
- HTTP: 401 alive / 29 gold
- HTTPS: 148 alive / 2 gold
- SOCKS4: 200 alive / 120 gold
- SOCKS5: 228 alive / 105 gold

## Historical pool

- Discovered: 99105
- Ever alive: 11745
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
