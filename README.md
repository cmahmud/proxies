# SyndProxy private pool

## Current pool

- Alive now: 1015
- Gold now: 416
- HTTP: 293 alive / 89 gold
- HTTPS: 214 alive / 21 gold
- SOCKS4: 228 alive / 146 gold
- SOCKS5: 280 alive / 160 gold

## Historical pool

- Discovered: 136206
- Ever alive: 22338
- Ever gold: 896

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
