# SyndProxy private pool

## Current pool

- Alive now: 1032
- Gold now: 425
- HTTP: 340 alive / 96 gold
- HTTPS: 191 alive / 28 gold
- SOCKS4: 234 alive / 144 gold
- SOCKS5: 267 alive / 157 gold

## Historical pool

- Discovered: 167127
- Ever alive: 32549
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
