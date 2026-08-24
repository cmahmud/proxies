# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 433
- HTTP: 131 alive / 77 gold
- HTTPS: 90 alive / 25 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34597
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
