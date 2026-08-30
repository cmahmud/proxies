# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 442
- HTTP: 116 alive / 79 gold
- HTTPS: 82 alive / 33 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 197 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44622
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
