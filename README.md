# SyndProxy private pool

## Current pool

- Alive now: 1183
- Gold now: 495
- HTTP: 384 alive / 120 gold
- HTTPS: 275 alive / 71 gold
- SOCKS4: 240 alive / 155 gold
- SOCKS5: 284 alive / 149 gold

## Historical pool

- Discovered: 114413
- Ever alive: 17039
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
