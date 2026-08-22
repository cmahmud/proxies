# SyndProxy private pool

## Current pool

- Alive now: 972
- Gold now: 367
- HTTP: 302 alive / 78 gold
- HTTPS: 226 alive / 24 gold
- SOCKS4: 206 alive / 137 gold
- SOCKS5: 238 alive / 128 gold

## Historical pool

- Discovered: 165836
- Ever alive: 32363
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
