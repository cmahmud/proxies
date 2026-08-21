# SyndProxy private pool

## Current pool

- Alive now: 946
- Gold now: 406
- HTTP: 271 alive / 92 gold
- HTTPS: 217 alive / 25 gold
- SOCKS4: 213 alive / 144 gold
- SOCKS5: 245 alive / 145 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29086
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
