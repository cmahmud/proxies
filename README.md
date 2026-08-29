# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 446
- HTTP: 129 alive / 90 gold
- HTTPS: 58 alive / 30 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 189 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43669
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
