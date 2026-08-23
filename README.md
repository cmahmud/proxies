# SyndProxy validated proxy pool

## Current pool

- Alive now: 337
- Gold now: 208
- HTTP: 107 alive / 42 gold
- HTTPS: 36 alive / 6 gold
- SOCKS4: 87 alive / 69 gold
- SOCKS5: 107 alive / 91 gold

## Historical pool

- Discovered: 170533
- Ever alive: 32763
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
