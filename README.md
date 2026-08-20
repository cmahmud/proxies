# SyndProxy private pool

## Current pool

- Alive now: 710
- Gold now: 373
- HTTP: 168 alive / 58 gold
- HTTPS: 116 alive / 17 gold
- SOCKS4: 198 alive / 148 gold
- SOCKS5: 228 alive / 150 gold

## Historical pool

- Discovered: 147647
- Ever alive: 25862
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
