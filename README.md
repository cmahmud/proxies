# SyndProxy private pool

## Current pool

- Alive now: 1123
- Gold now: 529
- HTTP: 447 alive / 188 gold
- HTTPS: 272 alive / 112 gold
- SOCKS4: 204 alive / 111 gold
- SOCKS5: 200 alive / 118 gold

## Historical pool

- Discovered: 124845
- Ever alive: 19386
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
