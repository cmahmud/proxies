# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 404
- HTTP: 98 alive / 63 gold
- HTTPS: 115 alive / 15 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 190 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41414
- Ever gold: 1327

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
