# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 415
- HTTP: 95 alive / 60 gold
- HTTPS: 96 alive / 22 gold
- SOCKS4: 184 alive / 167 gold
- SOCKS5: 192 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41533
- Ever gold: 1337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
