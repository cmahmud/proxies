# SyndProxy private pool

## Current pool

- Alive now: 957
- Gold now: 398
- HTTP: 311 alive / 105 gold
- HTTPS: 238 alive / 30 gold
- SOCKS4: 196 alive / 144 gold
- SOCKS5: 212 alive / 119 gold

## Historical pool

- Discovered: 153184
- Ever alive: 28480
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
