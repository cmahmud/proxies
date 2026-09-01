# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 415
- HTTP: 82 alive / 62 gold
- HTTPS: 47 alive / 21 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47119
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
