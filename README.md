# SyndProxy private pool

## Current pool

- Alive now: 954
- Gold now: 367
- HTTP: 324 alive / 84 gold
- HTTPS: 203 alive / 21 gold
- SOCKS4: 207 alive / 121 gold
- SOCKS5: 220 alive / 141 gold

## Historical pool

- Discovered: 158219
- Ever alive: 29811
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
