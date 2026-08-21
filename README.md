# SyndProxy private pool

## Current pool

- Alive now: 851
- Gold now: 413
- HTTP: 276 alive / 94 gold
- HTTPS: 156 alive / 22 gold
- SOCKS4: 204 alive / 146 gold
- SOCKS5: 215 alive / 151 gold

## Historical pool

- Discovered: 152160
- Ever alive: 27819
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
