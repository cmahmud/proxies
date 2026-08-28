# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 389
- HTTP: 74 alive / 56 gold
- HTTPS: 62 alive / 14 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 169 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42902
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
