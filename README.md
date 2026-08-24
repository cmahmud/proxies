# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 391
- HTTP: 118 alive / 71 gold
- HTTPS: 45 alive / 15 gold
- SOCKS4: 168 alive / 154 gold
- SOCKS5: 174 alive / 151 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33250
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
