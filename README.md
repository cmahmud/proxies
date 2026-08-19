# SyndProxy private pool

## Current pool

- Alive now: 1098
- Gold now: 402
- HTTP: 329 alive / 88 gold
- HTTPS: 228 alive / 14 gold
- SOCKS4: 251 alive / 148 gold
- SOCKS5: 290 alive / 152 gold

## Historical pool

- Discovered: 131828
- Ever alive: 21067
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
