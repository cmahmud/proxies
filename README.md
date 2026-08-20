# SyndProxy private pool

## Current pool

- Alive now: 926
- Gold now: 417
- HTTP: 250 alive / 97 gold
- HTTPS: 197 alive / 24 gold
- SOCKS4: 218 alive / 137 gold
- SOCKS5: 261 alive / 159 gold

## Historical pool

- Discovered: 151678
- Ever alive: 27594
- Ever gold: 1100

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
