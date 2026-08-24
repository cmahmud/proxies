# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 383
- HTTP: 148 alive / 63 gold
- HTTPS: 57 alive / 16 gold
- SOCKS4: 180 alive / 153 gold
- SOCKS5: 169 alive / 151 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33216
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
