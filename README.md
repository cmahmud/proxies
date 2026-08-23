# SyndProxy validated proxy pool

## Current pool

- Alive now: 377
- Gold now: 206
- HTTP: 114 alive / 48 gold
- HTTPS: 69 alive / 8 gold
- SOCKS4: 75 alive / 65 gold
- SOCKS5: 119 alive / 85 gold

## Historical pool

- Discovered: 169817
- Ever alive: 32700
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
