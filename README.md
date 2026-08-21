# SyndProxy private pool

## Current pool

- Alive now: 998
- Gold now: 413
- HTTP: 342 alive / 92 gold
- HTTPS: 201 alive / 24 gold
- SOCKS4: 207 alive / 151 gold
- SOCKS5: 248 alive / 146 gold

## Historical pool

- Discovered: 158253
- Ever alive: 30077
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
