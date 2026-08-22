# SyndProxy private pool

## Current pool

- Alive now: 1152
- Gold now: 394
- HTTP: 428 alive / 92 gold
- HTTPS: 266 alive / 22 gold
- SOCKS4: 195 alive / 112 gold
- SOCKS5: 263 alive / 168 gold

## Historical pool

- Discovered: 166620
- Ever alive: 32446
- Ever gold: 1182

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
