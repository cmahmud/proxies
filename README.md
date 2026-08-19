# SyndProxy private pool

## Current pool

- Alive now: 1315
- Gold now: 413
- HTTP: 426 alive / 82 gold
- HTTPS: 304 alive / 17 gold
- SOCKS4: 256 alive / 157 gold
- SOCKS5: 329 alive / 157 gold

## Historical pool

- Discovered: 134540
- Ever alive: 21968
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
