# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 418
- HTTP: 99 alive / 72 gold
- HTTPS: 101 alive / 22 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 187 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42622
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
