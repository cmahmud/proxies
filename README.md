# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 393
- HTTP: 100 alive / 62 gold
- HTTPS: 87 alive / 18 gold
- SOCKS4: 167 alive / 157 gold
- SOCKS5: 165 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37415
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
