# SyndProxy private pool

## Current pool

- Alive now: 1241
- Gold now: 400
- HTTP: 398 alive / 90 gold
- HTTPS: 280 alive / 12 gold
- SOCKS4: 264 alive / 142 gold
- SOCKS5: 299 alive / 156 gold

## Historical pool

- Discovered: 131826
- Ever alive: 21026
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
