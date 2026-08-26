# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 387
- HTTP: 117 alive / 68 gold
- HTTPS: 144 alive / 21 gold
- SOCKS4: 167 alive / 147 gold
- SOCKS5: 188 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39637
- Ever gold: 1300

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
