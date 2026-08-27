# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 398
- HTTP: 89 alive / 56 gold
- HTTPS: 107 alive / 12 gold
- SOCKS4: 184 alive / 167 gold
- SOCKS5: 189 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41525
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
