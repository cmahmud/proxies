# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 395
- HTTP: 117 alive / 70 gold
- HTTPS: 57 alive / 16 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 182 alive / 153 gold

## Historical pool

- Discovered: 176968
- Ever alive: 33260
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
