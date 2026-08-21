# SyndProxy private pool

## Current pool

- Alive now: 923
- Gold now: 408
- HTTP: 252 alive / 90 gold
- HTTPS: 200 alive / 23 gold
- SOCKS4: 229 alive / 146 gold
- SOCKS5: 242 alive / 149 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29092
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
