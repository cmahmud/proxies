# SyndProxy private pool

## Current pool

- Alive now: 913
- Gold now: 408
- HTTP: 234 alive / 87 gold
- HTTPS: 200 alive / 20 gold
- SOCKS4: 233 alive / 149 gold
- SOCKS5: 246 alive / 152 gold

## Historical pool

- Discovered: 151674
- Ever alive: 27568
- Ever gold: 1099

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
