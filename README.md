# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 414
- HTTP: 89 alive / 66 gold
- HTTPS: 55 alive / 17 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 178 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48853
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
