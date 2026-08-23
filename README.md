# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 347
- HTTP: 149 alive / 41 gold
- HTTPS: 39 alive / 8 gold
- SOCKS4: 163 alive / 153 gold
- SOCKS5: 168 alive / 145 gold

## Historical pool

- Discovered: 171087
- Ever alive: 32863
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
