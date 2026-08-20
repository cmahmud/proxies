# SyndProxy private pool

## Current pool

- Alive now: 942
- Gold now: 385
- HTTP: 291 alive / 78 gold
- HTTPS: 202 alive / 25 gold
- SOCKS4: 202 alive / 130 gold
- SOCKS5: 247 alive / 152 gold

## Historical pool

- Discovered: 144732
- Ever alive: 24938
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
