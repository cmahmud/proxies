# SyndProxy private pool

## Current pool

- Alive now: 762
- Gold now: 389
- HTTP: 224 alive / 87 gold
- HTTPS: 128 alive / 24 gold
- SOCKS4: 185 alive / 122 gold
- SOCKS5: 225 alive / 156 gold

## Historical pool

- Discovered: 156418
- Ever alive: 29471
- Ever gold: 1128

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
