# SyndProxy validated proxy pool

## Current pool

- Alive now: 684
- Gold now: 476
- HTTP: 163 alive / 99 gold
- HTTPS: 126 alive / 38 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 219 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45256
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
