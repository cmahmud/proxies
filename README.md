# SyndProxy private pool

## Current pool

- Alive now: 1214
- Gold now: 495
- HTTP: 383 alive / 120 gold
- HTTPS: 299 alive / 71 gold
- SOCKS4: 244 alive / 154 gold
- SOCKS5: 288 alive / 150 gold

## Historical pool

- Discovered: 114413
- Ever alive: 17035
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
