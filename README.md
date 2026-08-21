# SyndProxy private pool

## Current pool

- Alive now: 907
- Gold now: 412
- HTTP: 269 alive / 92 gold
- HTTPS: 171 alive / 25 gold
- SOCKS4: 218 alive / 148 gold
- SOCKS5: 249 alive / 147 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29115
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
