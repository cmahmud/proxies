# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 389
- HTTP: 110 alive / 71 gold
- HTTPS: 84 alive / 14 gold
- SOCKS4: 162 alive / 151 gold
- SOCKS5: 179 alive / 153 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33235
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
