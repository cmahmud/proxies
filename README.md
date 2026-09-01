# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 452
- HTTP: 108 alive / 80 gold
- HTTPS: 106 alive / 31 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 190 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47375
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
