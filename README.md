# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 347
- HTTP: 212 alive / 39 gold
- HTTPS: 44 alive / 9 gold
- SOCKS4: 179 alive / 154 gold
- SOCKS5: 199 alive / 145 gold

## Historical pool

- Discovered: 171088
- Ever alive: 32865
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
