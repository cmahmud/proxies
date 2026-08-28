# SyndProxy validated proxy pool

## Current pool

- Alive now: 460
- Gold now: 391
- HTTP: 76 alive / 54 gold
- HTTPS: 43 alive / 16 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 174 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42804
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
