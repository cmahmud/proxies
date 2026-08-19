# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 395
- HTTP: 302 alive / 73 gold
- HTTPS: 219 alive / 15 gold
- SOCKS4: 255 alive / 147 gold
- SOCKS5: 235 alive / 160 gold

## Historical pool

- Discovered: 129319
- Ever alive: 20476
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
