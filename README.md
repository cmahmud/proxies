# SyndProxy validated proxy pool

## Current pool

- Alive now: 371
- Gold now: 306
- HTTP: 80 alive / 60 gold
- HTTPS: 36 alive / 22 gold
- SOCKS4: 115 alive / 101 gold
- SOCKS5: 140 alive / 123 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49506
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
