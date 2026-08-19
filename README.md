# SyndProxy private pool

## Current pool

- Alive now: 962
- Gold now: 362
- HTTP: 334 alive / 67 gold
- HTTPS: 173 alive / 16 gold
- SOCKS4: 228 alive / 156 gold
- SOCKS5: 227 alive / 123 gold

## Historical pool

- Discovered: 111009
- Ever alive: 16105
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
