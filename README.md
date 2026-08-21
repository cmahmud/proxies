# SyndProxy private pool

## Current pool

- Alive now: 980
- Gold now: 402
- HTTP: 325 alive / 102 gold
- HTTPS: 243 alive / 29 gold
- SOCKS4: 203 alive / 147 gold
- SOCKS5: 209 alive / 124 gold

## Historical pool

- Discovered: 153184
- Ever alive: 28465
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
