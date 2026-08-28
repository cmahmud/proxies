# SyndProxy validated proxy pool

## Current pool

- Alive now: 454
- Gold now: 398
- HTTP: 76 alive / 58 gold
- HTTPS: 41 alive / 20 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 170 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42806
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
