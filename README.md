# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 415
- HTTP: 90 alive / 69 gold
- HTTPS: 83 alive / 21 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 178 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41753
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
