# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 415
- HTTP: 101 alive / 70 gold
- HTTPS: 84 alive / 23 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 173 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41776
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
