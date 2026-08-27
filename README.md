# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 402
- HTTP: 93 alive / 62 gold
- HTTPS: 109 alive / 15 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 193 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41415
- Ever gold: 1327

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
