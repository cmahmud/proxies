# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 446
- HTTP: 112 alive / 83 gold
- HTTPS: 50 alive / 30 gold
- SOCKS4: 167 alive / 162 gold
- SOCKS5: 186 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43681
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
