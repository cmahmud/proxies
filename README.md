# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 408
- HTTP: 95 alive / 65 gold
- HTTPS: 97 alive / 19 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 188 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42649
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
