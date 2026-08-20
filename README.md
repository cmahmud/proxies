# SyndProxy private pool

## Current pool

- Alive now: 1529
- Gold now: 556
- HTTP: 625 alive / 176 gold
- HTTPS: 422 alive / 91 gold
- SOCKS4: 235 alive / 131 gold
- SOCKS5: 247 alive / 158 gold

## Historical pool

- Discovered: 138827
- Ever alive: 23033
- Ever gold: 913

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
