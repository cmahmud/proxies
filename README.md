# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 398
- HTTP: 130 alive / 62 gold
- HTTPS: 70 alive / 14 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 183 alive / 163 gold

## Historical pool

- Discovered: 179712
- Ever alive: 33508
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
