# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 398
- HTTP: 123 alive / 73 gold
- HTTPS: 56 alive / 15 gold
- SOCKS4: 168 alive / 154 gold
- SOCKS5: 185 alive / 156 gold

## Historical pool

- Discovered: 176974
- Ever alive: 33270
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
