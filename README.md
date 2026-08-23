# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 349
- HTTP: 222 alive / 41 gold
- HTTPS: 46 alive / 9 gold
- SOCKS4: 182 alive / 153 gold
- SOCKS5: 192 alive / 146 gold

## Historical pool

- Discovered: 171088
- Ever alive: 32864
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
