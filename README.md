# SyndProxy private pool

## Current pool

- Alive now: 803
- Gold now: 356
- HTTP: 233 alive / 86 gold
- HTTPS: 156 alive / 28 gold
- SOCKS4: 186 alive / 105 gold
- SOCKS5: 228 alive / 137 gold

## Historical pool

- Discovered: 167356
- Ever alive: 32557
- Ever gold: 1188

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
