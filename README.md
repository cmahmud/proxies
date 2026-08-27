# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 389
- HTTP: 91 alive / 48 gold
- HTTPS: 49 alive / 17 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 186 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41672
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
