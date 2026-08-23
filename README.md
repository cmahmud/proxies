# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 360
- HTTP: 89 alive / 35 gold
- HTTPS: 47 alive / 11 gold
- SOCKS4: 167 alive / 154 gold
- SOCKS5: 182 alive / 160 gold

## Historical pool

- Discovered: 171600
- Ever alive: 32943
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
