# SyndProxy private pool

## Current pool

- Alive now: 911
- Gold now: 409
- HTTP: 271 alive / 90 gold
- HTTPS: 171 alive / 25 gold
- SOCKS4: 220 alive / 148 gold
- SOCKS5: 249 alive / 146 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29115
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
