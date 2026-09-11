# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 407
- HTTP: 84 alive / 62 gold
- HTTPS: 39 alive / 22 gold
- SOCKS4: 168 alive / 153 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48815
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
