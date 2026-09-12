# SyndProxy validated proxy pool

## Current pool

- Alive now: 365
- Gold now: 306
- HTTP: 77 alive / 58 gold
- HTTPS: 37 alive / 17 gold
- SOCKS4: 114 alive / 103 gold
- SOCKS5: 137 alive / 128 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49502
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
