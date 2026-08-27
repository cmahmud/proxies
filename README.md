# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 398
- HTTP: 115 alive / 59 gold
- HTTPS: 122 alive / 15 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41344
- Ever gold: 1325

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
