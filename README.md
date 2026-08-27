# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 415
- HTTP: 97 alive / 74 gold
- HTTPS: 112 alive / 22 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 175 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41827
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
