# SyndProxy private pool

## Current pool

- Alive now: 831
- Gold now: 404
- HTTP: 256 alive / 89 gold
- HTTPS: 149 alive / 20 gold
- SOCKS4: 208 alive / 138 gold
- SOCKS5: 218 alive / 157 gold

## Historical pool

- Discovered: 151679
- Ever alive: 27636
- Ever gold: 1102

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
