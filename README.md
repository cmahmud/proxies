# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 411
- HTTP: 96 alive / 66 gold
- HTTPS: 85 alive / 18 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42668
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
