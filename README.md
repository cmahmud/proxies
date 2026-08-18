# SyndProxy private pool

## Current pool

- Alive now: 738
- Gold now: 245
- HTTP: 220 alive / 27 gold
- HTTPS: 130 alive / 9 gold
- SOCKS4: 180 alive / 107 gold
- SOCKS5: 208 alive / 102 gold

## Historical pool

- Discovered: 95258
- Ever alive: 10188
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
