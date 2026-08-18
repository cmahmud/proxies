# SyndProxy private pool

## Current pool

- Alive now: 668
- Gold now: 218
- HTTP: 195 alive / 34 gold
- HTTPS: 111 alive / 10 gold
- SOCKS4: 183 alive / 101 gold
- SOCKS5: 179 alive / 73 gold

## Historical pool

- Discovered: 86649
- Ever alive: 5725
- Ever gold: 292

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
