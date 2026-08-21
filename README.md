# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 413
- HTTP: 308 alive / 84 gold
- HTTPS: 230 alive / 26 gold
- SOCKS4: 202 alive / 149 gold
- SOCKS5: 242 alive / 154 gold

## Historical pool

- Discovered: 158231
- Ever alive: 29924
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
