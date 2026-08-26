# SyndProxy validated proxy pool

## Current pool

- Alive now: 661
- Gold now: 398
- HTTP: 167 alive / 69 gold
- HTTPS: 127 alive / 23 gold
- SOCKS4: 164 alive / 150 gold
- SOCKS5: 203 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39513
- Ever gold: 1298

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
