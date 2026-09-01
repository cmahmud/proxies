# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 445
- HTTP: 96 alive / 76 gold
- HTTPS: 92 alive / 30 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 188 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47364
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
