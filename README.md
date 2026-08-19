# SyndProxy private pool

## Current pool

- Alive now: 1085
- Gold now: 513
- HTTP: 408 alive / 179 gold
- HTTPS: 302 alive / 116 gold
- SOCKS4: 196 alive / 105 gold
- SOCKS5: 179 alive / 113 gold

## Historical pool

- Discovered: 124841
- Ever alive: 19320
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
