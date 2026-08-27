# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 414
- HTTP: 107 alive / 72 gold
- HTTPS: 106 alive / 23 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 177 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41868
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
