# SyndProxy validated proxy pool

## Current pool

- Alive now: 597
- Gold now: 414
- HTTP: 109 alive / 67 gold
- HTTPS: 129 alive / 17 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41337
- Ever gold: 1325

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
