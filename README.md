# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 415
- HTTP: 114 alive / 74 gold
- HTTPS: 75 alive / 17 gold
- SOCKS4: 163 alive / 158 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33736
- Ever gold: 1249

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
