# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 398
- HTTP: 125 alive / 72 gold
- HTTPS: 52 alive / 16 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 184 alive / 154 gold

## Historical pool

- Discovered: 176968
- Ever alive: 33261
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
