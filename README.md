# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 405
- HTTP: 93 alive / 62 gold
- HTTPS: 56 alive / 22 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 184 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41712
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
