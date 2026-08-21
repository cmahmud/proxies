# SyndProxy private pool

## Current pool

- Alive now: 904
- Gold now: 403
- HTTP: 259 alive / 95 gold
- HTTPS: 216 alive / 25 gold
- SOCKS4: 226 alive / 158 gold
- SOCKS5: 203 alive / 125 gold

## Historical pool

- Discovered: 160982
- Ever alive: 30859
- Ever gold: 1150

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
