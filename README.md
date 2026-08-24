# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 389
- HTTP: 98 alive / 60 gold
- HTTPS: 37 alive / 11 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 185 alive / 159 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33317
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
