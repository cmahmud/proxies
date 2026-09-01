# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 454
- HTTP: 138 alive / 84 gold
- HTTPS: 123 alive / 32 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 198 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46837
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
