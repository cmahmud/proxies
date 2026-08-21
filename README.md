# SyndProxy private pool

## Current pool

- Alive now: 791
- Gold now: 419
- HTTP: 210 alive / 93 gold
- HTTPS: 156 alive / 25 gold
- SOCKS4: 213 alive / 140 gold
- SOCKS5: 212 alive / 161 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27720
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
