# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 445
- HTTP: 90 alive / 73 gold
- HTTPS: 105 alive / 32 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 190 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47437
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
