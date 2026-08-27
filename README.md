# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 398
- HTTP: 79 alive / 55 gold
- HTTPS: 54 alive / 17 gold
- SOCKS4: 181 alive / 163 gold
- SOCKS5: 181 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41577
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
