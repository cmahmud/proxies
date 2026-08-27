# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 414
- HTTP: 98 alive / 71 gold
- HTTPS: 120 alive / 23 gold
- SOCKS4: 168 alive / 157 gold
- SOCKS5: 182 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41898
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
