# SyndProxy validated proxy pool

## Current pool

- Alive now: 681
- Gold now: 469
- HTTP: 166 alive / 96 gold
- HTTPS: 126 alive / 36 gold
- SOCKS4: 183 alive / 163 gold
- SOCKS5: 206 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45251
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
