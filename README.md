# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 381
- HTTP: 119 alive / 69 gold
- HTTPS: 152 alive / 15 gold
- SOCKS4: 159 alive / 147 gold
- SOCKS5: 169 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39779
- Ever gold: 1303

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
