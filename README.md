# SyndProxy private pool

## Current pool

- Alive now: 914
- Gold now: 306
- HTTP: 296 alive / 63 gold
- HTTPS: 232 alive / 19 gold
- SOCKS4: 189 alive / 117 gold
- SOCKS5: 197 alive / 107 gold

## Historical pool

- Discovered: 109961
- Ever alive: 15462
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
