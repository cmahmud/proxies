# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 194
- HTTP: 156 alive / 41 gold
- HTTPS: 43 alive / 8 gold
- SOCKS4: 138 alive / 64 gold
- SOCKS5: 126 alive / 81 gold

## Historical pool

- Discovered: 170278
- Ever alive: 32720
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
