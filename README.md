# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 402
- HTTP: 113 alive / 69 gold
- HTTPS: 62 alive / 10 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 184 alive / 163 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33310
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
