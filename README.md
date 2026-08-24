# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 415
- HTTP: 112 alive / 75 gold
- HTTPS: 76 alive / 17 gold
- SOCKS4: 161 alive / 158 gold
- SOCKS5: 188 alive / 165 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33735
- Ever gold: 1249

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
