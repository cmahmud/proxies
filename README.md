# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 398
- HTTP: 128 alive / 67 gold
- HTTPS: 45 alive / 11 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 194 alive / 161 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33314
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
