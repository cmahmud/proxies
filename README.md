# SyndProxy private pool

## Current pool

- Alive now: 856
- Gold now: 342
- HTTP: 283 alive / 79 gold
- HTTPS: 182 alive / 31 gold
- SOCKS4: 196 alive / 137 gold
- SOCKS5: 195 alive / 95 gold

## Historical pool

- Discovered: 167111
- Ever alive: 32515
- Ever gold: 1184

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
