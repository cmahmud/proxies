# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 399
- HTTP: 94 alive / 58 gold
- HTTPS: 52 alive / 20 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 183 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41707
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
