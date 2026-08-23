# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 347
- HTTP: 172 alive / 41 gold
- HTTPS: 40 alive / 8 gold
- SOCKS4: 166 alive / 153 gold
- SOCKS5: 170 alive / 145 gold

## Historical pool

- Discovered: 171087
- Ever alive: 32864
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
