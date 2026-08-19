# SyndProxy private pool

## Current pool

- Alive now: 1005
- Gold now: 362
- HTTP: 304 alive / 70 gold
- HTTPS: 241 alive / 18 gold
- SOCKS4: 228 alive / 153 gold
- SOCKS5: 232 alive / 121 gold

## Historical pool

- Discovered: 111009
- Ever alive: 16104
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
