# SyndProxy private pool

## Current pool

- Alive now: 765
- Gold now: 391
- HTTP: 229 alive / 90 gold
- HTTPS: 126 alive / 23 gold
- SOCKS4: 182 alive / 122 gold
- SOCKS5: 228 alive / 156 gold

## Historical pool

- Discovered: 156418
- Ever alive: 29471
- Ever gold: 1128

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
