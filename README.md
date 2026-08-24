# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 399
- HTTP: 129 alive / 73 gold
- HTTPS: 53 alive / 16 gold
- SOCKS4: 171 alive / 156 gold
- SOCKS5: 184 alive / 154 gold

## Historical pool

- Discovered: 176968
- Ever alive: 33261
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
