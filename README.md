# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 405
- HTTP: 106 alive / 61 gold
- HTTPS: 160 alive / 13 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 193 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40764
- Ever gold: 1312

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
