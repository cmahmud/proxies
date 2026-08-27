# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 417
- HTTP: 105 alive / 77 gold
- HTTPS: 121 alive / 21 gold
- SOCKS4: 166 alive / 157 gold
- SOCKS5: 183 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41856
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
