# SyndProxy private pool

## Current pool

- Alive now: 892
- Gold now: 391
- HTTP: 279 alive / 79 gold
- HTTPS: 188 alive / 19 gold
- SOCKS4: 196 alive / 131 gold
- SOCKS5: 229 alive / 162 gold

## Historical pool

- Discovered: 157412
- Ever alive: 29686
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
