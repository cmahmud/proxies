# SyndProxy private pool

## Current pool

- Alive now: 1091
- Gold now: 391
- HTTP: 384 alive / 89 gold
- HTTPS: 264 alive / 22 gold
- SOCKS4: 185 alive / 112 gold
- SOCKS5: 258 alive / 168 gold

## Historical pool

- Discovered: 166620
- Ever alive: 32445
- Ever gold: 1182

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
