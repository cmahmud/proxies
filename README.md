# SyndProxy private pool

## Current pool

- Alive now: 898
- Gold now: 414
- HTTP: 261 alive / 92 gold
- HTTPS: 170 alive / 25 gold
- SOCKS4: 220 alive / 148 gold
- SOCKS5: 247 alive / 149 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29115
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
