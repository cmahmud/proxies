# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 405
- HTTP: 88 alive / 62 gold
- HTTPS: 42 alive / 20 gold
- SOCKS4: 165 alive / 156 gold
- SOCKS5: 177 alive / 167 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48840
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
