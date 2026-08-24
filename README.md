# SyndProxy validated proxy pool

## Current pool

- Alive now: 583
- Gold now: 415
- HTTP: 148 alive / 74 gold
- HTTPS: 64 alive / 19 gold
- SOCKS4: 177 alive / 158 gold
- SOCKS5: 194 alive / 164 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33742
- Ever gold: 1249

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
