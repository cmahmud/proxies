# SyndProxy private pool

## Current pool

- Alive now: 1132
- Gold now: 380
- HTTP: 360 alive / 76 gold
- HTTPS: 286 alive / 18 gold
- SOCKS4: 229 alive / 124 gold
- SOCKS5: 257 alive / 162 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15894
- Ever gold: 506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
