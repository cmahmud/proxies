# SyndProxy private pool

## Current pool

- Alive now: 1146
- Gold now: 392
- HTTP: 377 alive / 88 gold
- HTTPS: 264 alive / 22 gold
- SOCKS4: 210 alive / 133 gold
- SOCKS5: 295 alive / 149 gold

## Historical pool

- Discovered: 134558
- Ever alive: 22154
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
