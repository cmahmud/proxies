# SyndProxy private pool

## Current pool

- Alive now: 852
- Gold now: 395
- HTTP: 251 alive / 91 gold
- HTTPS: 162 alive / 29 gold
- SOCKS4: 214 alive / 140 gold
- SOCKS5: 225 alive / 135 gold

## Historical pool

- Discovered: 163259
- Ever alive: 31778
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
