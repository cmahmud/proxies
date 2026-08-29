# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 390
- HTTP: 85 alive / 62 gold
- HTTPS: 71 alive / 13 gold
- SOCKS4: 164 alive / 158 gold
- SOCKS5: 171 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43408
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
