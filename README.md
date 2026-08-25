# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 415
- HTTP: 100 alive / 61 gold
- HTTPS: 88 alive / 24 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35794
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
