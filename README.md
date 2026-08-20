# SyndProxy private pool

## Current pool

- Alive now: 817
- Gold now: 382
- HTTP: 218 alive / 78 gold
- HTTPS: 189 alive / 20 gold
- SOCKS4: 196 alive / 147 gold
- SOCKS5: 214 alive / 137 gold

## Historical pool

- Discovered: 149510
- Ever alive: 26838
- Ever gold: 1088

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
