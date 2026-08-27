# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 410
- HTTP: 111 alive / 63 gold
- HTTPS: 165 alive / 16 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40992
- Ever gold: 1315

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
