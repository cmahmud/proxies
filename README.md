# SyndProxy private pool

## Current pool

- Alive now: 813
- Gold now: 387
- HTTP: 227 alive / 90 gold
- HTTPS: 158 alive / 25 gold
- SOCKS4: 208 alive / 140 gold
- SOCKS5: 220 alive / 132 gold

## Historical pool

- Discovered: 163259
- Ever alive: 31778
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
