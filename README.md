# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 416
- HTTP: 100 alive / 71 gold
- HTTPS: 82 alive / 22 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 174 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41776
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
