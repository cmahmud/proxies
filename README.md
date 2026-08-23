# SyndProxy validated proxy pool

## Current pool

- Alive now: 452
- Gold now: 366
- HTTP: 75 alive / 40 gold
- HTTPS: 29 alive / 11 gold
- SOCKS4: 169 alive / 153 gold
- SOCKS5: 179 alive / 162 gold

## Historical pool

- Discovered: 172855
- Ever alive: 32986
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
