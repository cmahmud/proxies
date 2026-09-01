# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 446
- HTTP: 96 alive / 76 gold
- HTTPS: 94 alive / 30 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 190 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47364
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
