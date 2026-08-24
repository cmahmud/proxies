# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 408
- HTTP: 110 alive / 71 gold
- HTTPS: 74 alive / 18 gold
- SOCKS4: 165 alive / 156 gold
- SOCKS5: 191 alive / 163 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33724
- Ever gold: 1249

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
