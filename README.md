# SyndProxy validated proxy pool

## Current pool

- Alive now: 468
- Gold now: 347
- HTTP: 110 alive / 41 gold
- HTTPS: 38 alive / 9 gold
- SOCKS4: 157 alive / 153 gold
- SOCKS5: 163 alive / 144 gold

## Historical pool

- Discovered: 171087
- Ever alive: 32860
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
