# SyndProxy private pool

## Current pool

- Alive now: 1026
- Gold now: 413
- HTTP: 332 alive / 87 gold
- HTTPS: 235 alive / 27 gold
- SOCKS4: 218 alive / 143 gold
- SOCKS5: 241 alive / 156 gold

## Historical pool

- Discovered: 159211
- Ever alive: 30193
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
