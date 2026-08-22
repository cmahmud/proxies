# SyndProxy private pool

## Current pool

- Alive now: 866
- Gold now: 413
- HTTP: 253 alive / 86 gold
- HTTPS: 181 alive / 28 gold
- SOCKS4: 179 alive / 131 gold
- SOCKS5: 253 alive / 168 gold

## Historical pool

- Discovered: 162742
- Ever alive: 31492
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
