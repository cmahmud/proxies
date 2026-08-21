# SyndProxy private pool

## Current pool

- Alive now: 843
- Gold now: 416
- HTTP: 212 alive / 81 gold
- HTTPS: 144 alive / 27 gold
- SOCKS4: 220 alive / 143 gold
- SOCKS5: 267 alive / 165 gold

## Historical pool

- Discovered: 155796
- Ever alive: 29338
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
