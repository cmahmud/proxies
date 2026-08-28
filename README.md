# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 415
- HTTP: 104 alive / 71 gold
- HTTPS: 116 alive / 18 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42535
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
