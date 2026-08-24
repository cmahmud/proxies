# SyndProxy validated proxy pool

## Current pool

- Alive now: 577
- Gold now: 396
- HTTP: 160 alive / 67 gold
- HTTPS: 63 alive / 15 gold
- SOCKS4: 169 alive / 154 gold
- SOCKS5: 185 alive / 160 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33285
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
