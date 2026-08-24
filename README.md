# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 399
- HTTP: 133 alive / 65 gold
- HTTPS: 50 alive / 10 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 207 alive / 164 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33313
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
