# SyndProxy private pool

## Current pool

- Alive now: 833
- Gold now: 413
- HTTP: 240 alive / 85 gold
- HTTPS: 153 alive / 28 gold
- SOCKS4: 189 alive / 131 gold
- SOCKS5: 251 alive / 169 gold

## Historical pool

- Discovered: 162742
- Ever alive: 31495
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
