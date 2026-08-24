# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 396
- HTTP: 124 alive / 71 gold
- HTTPS: 54 alive / 16 gold
- SOCKS4: 169 alive / 156 gold
- SOCKS5: 183 alive / 153 gold

## Historical pool

- Discovered: 176968
- Ever alive: 33260
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
