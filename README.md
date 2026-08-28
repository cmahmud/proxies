# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 412
- HTTP: 94 alive / 66 gold
- HTTPS: 93 alive / 18 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42667
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
