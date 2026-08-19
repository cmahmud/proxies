# SyndProxy private pool

## Current pool

- Alive now: 992
- Gold now: 365
- HTTP: 295 alive / 73 gold
- HTTPS: 234 alive / 18 gold
- SOCKS4: 251 alive / 152 gold
- SOCKS5: 212 alive / 122 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15927
- Ever gold: 506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
