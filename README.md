# SyndProxy private pool

## Current pool

- Alive now: 903
- Gold now: 413
- HTTP: 231 alive / 90 gold
- HTTPS: 252 alive / 19 gold
- SOCKS4: 202 alive / 152 gold
- SOCKS5: 218 alive / 152 gold

## Historical pool

- Discovered: 151674
- Ever alive: 27554
- Ever gold: 1099

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
