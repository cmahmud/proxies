# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 398
- HTTP: 318 alive / 87 gold
- HTTPS: 235 alive / 23 gold
- SOCKS4: 207 alive / 132 gold
- SOCKS5: 283 alive / 156 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25033
- Ever gold: 1053

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
