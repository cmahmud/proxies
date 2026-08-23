# SyndProxy validated proxy pool

## Current pool

- Alive now: 667
- Gold now: 347
- HTTP: 239 alive / 40 gold
- HTTPS: 45 alive / 9 gold
- SOCKS4: 184 alive / 153 gold
- SOCKS5: 199 alive / 145 gold

## Historical pool

- Discovered: 171088
- Ever alive: 32864
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
