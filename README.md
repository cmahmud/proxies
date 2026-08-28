# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 409
- HTTP: 86 alive / 62 gold
- HTTPS: 92 alive / 21 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42687
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
