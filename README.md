# SyndProxy validated proxy pool

## Current pool

- Alive now: 678
- Gold now: 414
- HTTP: 130 alive / 66 gold
- HTTPS: 180 alive / 15 gold
- SOCKS4: 180 alive / 159 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40825
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
