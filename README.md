# SyndProxy private pool

## Current pool

- Alive now: 959
- Gold now: 413
- HTTP: 314 alive / 83 gold
- HTTPS: 199 alive / 26 gold
- SOCKS4: 189 alive / 133 gold
- SOCKS5: 257 alive / 171 gold

## Historical pool

- Discovered: 162742
- Ever alive: 31474
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
