# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 389
- HTTP: 95 alive / 61 gold
- HTTPS: 36 alive / 11 gold
- SOCKS4: 167 alive / 156 gold
- SOCKS5: 176 alive / 161 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33438
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
