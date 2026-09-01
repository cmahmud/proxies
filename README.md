# SyndProxy validated proxy pool

## Current pool

- Alive now: 609
- Gold now: 447
- HTTP: 125 alive / 81 gold
- HTTPS: 123 alive / 32 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 188 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46844
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
