# SyndProxy private pool

## Current pool

- Alive now: 760
- Gold now: 414
- HTTP: 202 alive / 89 gold
- HTTPS: 147 alive / 22 gold
- SOCKS4: 202 alive / 147 gold
- SOCKS5: 209 alive / 156 gold

## Historical pool

- Discovered: 151067
- Ever alive: 27413
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
