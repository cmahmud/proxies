# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 411
- HTTP: 91 alive / 68 gold
- HTTPS: 84 alive / 18 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 186 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42683
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
