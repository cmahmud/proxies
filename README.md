# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 374
- HTTP: 126 alive / 66 gold
- HTTPS: 60 alive / 14 gold
- SOCKS4: 171 alive / 147 gold
- SOCKS5: 180 alive / 147 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33221
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
