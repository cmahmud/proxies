# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 447
- HTTP: 134 alive / 91 gold
- HTTPS: 73 alive / 33 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 208 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44169
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
