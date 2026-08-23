# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 366
- HTTP: 86 alive / 42 gold
- HTTPS: 35 alive / 10 gold
- SOCKS4: 173 alive / 155 gold
- SOCKS5: 180 alive / 159 gold

## Historical pool

- Discovered: 173050
- Ever alive: 32990
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
