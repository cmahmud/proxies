# SyndProxy validated proxy pool

## Current pool

- Alive now: 433
- Gold now: 349
- HTTP: 120 alive / 81 gold
- HTTPS: 51 alive / 22 gold
- SOCKS4: 80 alive / 75 gold
- SOCKS5: 182 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48658
- Ever gold: 1563

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
