# SyndProxy private pool

## Current pool

- Alive now: 1130
- Gold now: 400
- HTTP: 383 alive / 79 gold
- HTTPS: 261 alive / 24 gold
- SOCKS4: 225 alive / 149 gold
- SOCKS5: 261 alive / 148 gold

## Historical pool

- Discovered: 158235
- Ever alive: 29970
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
