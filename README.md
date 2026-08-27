# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 415
- HTTP: 96 alive / 70 gold
- HTTPS: 116 alive / 18 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 195 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41406
- Ever gold: 1327

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
