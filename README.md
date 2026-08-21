# SyndProxy private pool

## Current pool

- Alive now: 772
- Gold now: 389
- HTTP: 229 alive / 86 gold
- HTTPS: 130 alive / 22 gold
- SOCKS4: 184 alive / 123 gold
- SOCKS5: 229 alive / 158 gold

## Historical pool

- Discovered: 156418
- Ever alive: 29471
- Ever gold: 1128

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
