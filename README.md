# SyndProxy private pool

## Current pool

- Alive now: 1199
- Gold now: 533
- HTTP: 452 alive / 157 gold
- HTTPS: 330 alive / 108 gold
- SOCKS4: 222 alive / 143 gold
- SOCKS5: 195 alive / 125 gold

## Historical pool

- Discovered: 127372
- Ever alive: 19945
- Ever gold: 804

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
