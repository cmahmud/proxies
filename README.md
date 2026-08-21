# SyndProxy private pool

## Current pool

- Alive now: 837
- Gold now: 418
- HTTP: 236 alive / 88 gold
- HTTPS: 124 alive / 20 gold
- SOCKS4: 234 alive / 154 gold
- SOCKS5: 243 alive / 156 gold

## Historical pool

- Discovered: 157425
- Ever alive: 29752
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
