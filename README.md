# SyndProxy private pool

## Current pool

- Alive now: 844
- Gold now: 390
- HTTP: 251 alive / 89 gold
- HTTPS: 154 alive / 28 gold
- SOCKS4: 212 alive / 140 gold
- SOCKS5: 227 alive / 133 gold

## Historical pool

- Discovered: 163259
- Ever alive: 31778
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
