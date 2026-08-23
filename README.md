# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 373
- HTTP: 108 alive / 48 gold
- HTTPS: 35 alive / 10 gold
- SOCKS4: 191 alive / 156 gold
- SOCKS5: 209 alive / 159 gold

## Historical pool

- Discovered: 173050
- Ever alive: 32991
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
