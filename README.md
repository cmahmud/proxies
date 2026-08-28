# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 415
- HTTP: 97 alive / 69 gold
- HTTPS: 93 alive / 19 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42624
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
