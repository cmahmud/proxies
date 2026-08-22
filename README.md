# SyndProxy private pool

## Current pool

- Alive now: 1135
- Gold now: 395
- HTTP: 453 alive / 90 gold
- HTTPS: 240 alive / 23 gold
- SOCKS4: 188 alive / 113 gold
- SOCKS5: 254 alive / 169 gold

## Historical pool

- Discovered: 166620
- Ever alive: 32448
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
