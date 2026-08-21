# SyndProxy private pool

## Current pool

- Alive now: 956
- Gold now: 404
- HTTP: 289 alive / 98 gold
- HTTPS: 205 alive / 29 gold
- SOCKS4: 226 alive / 156 gold
- SOCKS5: 236 alive / 121 gold

## Historical pool

- Discovered: 160286
- Ever alive: 30808
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
