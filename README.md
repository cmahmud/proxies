# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 412
- HTTP: 101 alive / 67 gold
- HTTPS: 92 alive / 19 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 188 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42673
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
