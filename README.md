# SyndProxy private pool

## Current pool

- Alive now: 824
- Gold now: 410
- HTTP: 220 alive / 90 gold
- HTTPS: 160 alive / 23 gold
- SOCKS4: 203 alive / 145 gold
- SOCKS5: 241 alive / 152 gold

## Historical pool

- Discovered: 152160
- Ever alive: 27811
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
