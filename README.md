# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 398
- HTTP: 110 alive / 75 gold
- HTTPS: 77 alive / 12 gold
- SOCKS4: 156 alive / 154 gold
- SOCKS5: 166 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43116
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
