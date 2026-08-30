# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 448
- HTTP: 127 alive / 89 gold
- HTTPS: 54 alive / 30 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43674
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
