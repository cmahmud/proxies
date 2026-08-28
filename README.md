# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 417
- HTTP: 106 alive / 71 gold
- HTTPS: 121 alive / 19 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42535
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
