# SyndProxy private pool

## Current pool

- Alive now: 992
- Gold now: 398
- HTTP: 304 alive / 74 gold
- HTTPS: 202 alive / 17 gold
- SOCKS4: 242 alive / 151 gold
- SOCKS5: 244 alive / 156 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15899
- Ever gold: 506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
