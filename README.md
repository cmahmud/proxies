# SyndProxy private pool

## Current pool

- Alive now: 991
- Gold now: 377
- HTTP: 333 alive / 73 gold
- HTTPS: 218 alive / 18 gold
- SOCKS4: 199 alive / 125 gold
- SOCKS5: 241 alive / 161 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15763
- Ever gold: 504

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
