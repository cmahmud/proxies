# SyndProxy validated proxy pool

## Current pool

- Alive now: 465
- Gold now: 356
- HTTP: 71 alive / 49 gold
- HTTPS: 55 alive / 9 gold
- SOCKS4: 167 alive / 145 gold
- SOCKS5: 172 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43507
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
