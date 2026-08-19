# SyndProxy private pool

## Current pool

- Alive now: 1076
- Gold now: 379
- HTTP: 313 alive / 73 gold
- HTTPS: 279 alive / 18 gold
- SOCKS4: 227 alive / 125 gold
- SOCKS5: 257 alive / 163 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15894
- Ever gold: 506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
