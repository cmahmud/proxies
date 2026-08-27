# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 415
- HTTP: 100 alive / 75 gold
- HTTPS: 98 alive / 22 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 181 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41839
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
