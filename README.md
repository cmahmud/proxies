# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 392
- HTTP: 110 alive / 64 gold
- HTTPS: 57 alive / 13 gold
- SOCKS4: 168 alive / 154 gold
- SOCKS5: 182 alive / 161 gold

## Historical pool

- Discovered: 175438
- Ever alive: 33156
- Ever gold: 1228

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
