# SyndProxy private pool

## Current pool

- Alive now: 1744
- Gold now: 612
- HTTP: 756 alive / 226 gold
- HTTPS: 575 alive / 119 gold
- SOCKS4: 172 alive / 104 gold
- SOCKS5: 241 alive / 163 gold

## Historical pool

- Discovered: 143486
- Ever alive: 24762
- Ever gold: 1037

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
