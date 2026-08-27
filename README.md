# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 399
- HTTP: 102 alive / 58 gold
- HTTPS: 55 alive / 21 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 183 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41709
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
