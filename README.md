# SyndProxy validated proxy pool

## Current pool

- Alive now: 705
- Gold now: 347
- HTTP: 208 alive / 39 gold
- HTTPS: 52 alive / 9 gold
- SOCKS4: 190 alive / 154 gold
- SOCKS5: 255 alive / 145 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32872
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
