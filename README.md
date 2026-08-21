# SyndProxy private pool

## Current pool

- Alive now: 996
- Gold now: 416
- HTTP: 331 alive / 112 gold
- HTTPS: 226 alive / 33 gold
- SOCKS4: 210 alive / 137 gold
- SOCKS5: 229 alive / 134 gold

## Historical pool

- Discovered: 160276
- Ever alive: 30746
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
