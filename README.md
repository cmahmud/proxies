# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 398
- HTTP: 137 alive / 64 gold
- HTTPS: 49 alive / 11 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 203 alive / 163 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33313
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
