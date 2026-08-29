# SyndProxy validated proxy pool

## Current pool

- Alive now: 397
- Gold now: 334
- HTTP: 63 alive / 36 gold
- HTTPS: 34 alive / 7 gold
- SOCKS4: 151 alive / 146 gold
- SOCKS5: 149 alive / 145 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43634
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
