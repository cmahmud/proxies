# SyndProxy private pool

## Current pool

- Alive now: 1166
- Gold now: 409
- HTTP: 410 alive / 92 gold
- HTTPS: 243 alive / 18 gold
- SOCKS4: 228 alive / 143 gold
- SOCKS5: 285 alive / 156 gold

## Historical pool

- Discovered: 131817
- Ever alive: 20872
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
