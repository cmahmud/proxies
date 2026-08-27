# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 409
- HTTP: 108 alive / 64 gold
- HTTPS: 170 alive / 15 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40991
- Ever gold: 1315

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
