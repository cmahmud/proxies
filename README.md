# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 451
- HTTP: 108 alive / 79 gold
- HTTPS: 99 alive / 31 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 190 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47375
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
