# SyndProxy private pool

## Current pool

- Alive now: 1103
- Gold now: 388
- HTTP: 400 alive / 80 gold
- HTTPS: 231 alive / 21 gold
- SOCKS4: 230 alive / 126 gold
- SOCKS5: 242 alive / 161 gold

## Historical pool

- Discovered: 164969
- Ever alive: 32247
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
