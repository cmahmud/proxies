# SyndProxy validated proxy pool

## Current pool

- Alive now: 673
- Gold now: 407
- HTTP: 134 alive / 71 gold
- HTTPS: 167 alive / 14 gold
- SOCKS4: 176 alive / 157 gold
- SOCKS5: 196 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40536
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
