# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 430
- HTTP: 115 alive / 85 gold
- HTTPS: 158 alive / 19 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 196 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42178
- Ever gold: 1353

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
