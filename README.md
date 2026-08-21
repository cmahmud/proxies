# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 401
- HTTP: 321 alive / 108 gold
- HTTPS: 247 alive / 30 gold
- SOCKS4: 200 alive / 144 gold
- SOCKS5: 214 alive / 119 gold

## Historical pool

- Discovered: 153184
- Ever alive: 28488
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
