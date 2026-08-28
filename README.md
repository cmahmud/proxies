# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 405
- HTTP: 87 alive / 60 gold
- HTTPS: 91 alive / 19 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 183 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42639
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
