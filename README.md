# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 416
- HTTP: 99 alive / 70 gold
- HTTPS: 96 alive / 21 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42622
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
