# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 414
- HTTP: 114 alive / 75 gold
- HTTPS: 60 alive / 28 gold
- SOCKS4: 156 alive / 153 gold
- SOCKS5: 170 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43654
- Ever gold: 1376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
