# SyndProxy validated proxy pool

## Current pool

- Alive now: 343
- Gold now: 208
- HTTP: 113 alive / 44 gold
- HTTPS: 37 alive / 6 gold
- SOCKS4: 86 alive / 67 gold
- SOCKS5: 107 alive / 91 gold

## Historical pool

- Discovered: 170533
- Ever alive: 32763
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
