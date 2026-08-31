# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 477
- HTTP: 138 alive / 101 gold
- HTTPS: 124 alive / 39 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 203 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45085
- Ever gold: 1423

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
