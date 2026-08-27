# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 412
- HTTP: 108 alive / 63 gold
- HTTPS: 149 alive / 19 gold
- SOCKS4: 180 alive / 164 gold
- SOCKS5: 182 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41264
- Ever gold: 1320

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
