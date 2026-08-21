# SyndProxy private pool

## Current pool

- Alive now: 872
- Gold now: 409
- HTTP: 243 alive / 89 gold
- HTTPS: 171 alive / 24 gold
- SOCKS4: 213 alive / 148 gold
- SOCKS5: 245 alive / 148 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29115
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
