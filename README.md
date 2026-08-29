# SyndProxy validated proxy pool

## Current pool

- Alive now: 415
- Gold now: 362
- HTTP: 49 alive / 38 gold
- HTTPS: 31 alive / 3 gold
- SOCKS4: 161 alive / 157 gold
- SOCKS5: 174 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43563
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
