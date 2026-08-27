# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 396
- HTTP: 112 alive / 58 gold
- HTTPS: 129 alive / 14 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 183 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41342
- Ever gold: 1325

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
