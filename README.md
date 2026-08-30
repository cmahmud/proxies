# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 445
- HTTP: 114 alive / 82 gold
- HTTPS: 72 alive / 33 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 192 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44601
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
