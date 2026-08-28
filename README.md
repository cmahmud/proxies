# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 406
- HTTP: 99 alive / 64 gold
- HTTPS: 102 alive / 16 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42665
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
