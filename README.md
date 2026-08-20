# SyndProxy private pool

## Current pool

- Alive now: 1679
- Gold now: 556
- HTTP: 722 alive / 194 gold
- HTTPS: 545 alive / 95 gold
- SOCKS4: 174 alive / 104 gold
- SOCKS5: 238 alive / 163 gold

## Historical pool

- Discovered: 143486
- Ever alive: 24760
- Ever gold: 1037

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
