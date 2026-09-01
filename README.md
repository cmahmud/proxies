# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 445
- HTTP: 107 alive / 78 gold
- HTTPS: 103 alive / 31 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 185 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47377
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
