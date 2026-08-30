# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 441
- HTTP: 108 alive / 79 gold
- HTTPS: 88 alive / 33 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 197 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44609
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
