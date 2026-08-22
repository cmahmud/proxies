# SyndProxy private pool

## Current pool

- Alive now: 1108
- Gold now: 389
- HTTP: 403 alive / 80 gold
- HTTPS: 226 alive / 22 gold
- SOCKS4: 233 alive / 126 gold
- SOCKS5: 246 alive / 161 gold

## Historical pool

- Discovered: 164970
- Ever alive: 32247
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
