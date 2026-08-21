# SyndProxy private pool

## Current pool

- Alive now: 992
- Gold now: 390
- HTTP: 357 alive / 84 gold
- HTTPS: 177 alive / 20 gold
- SOCKS4: 203 alive / 128 gold
- SOCKS5: 255 alive / 158 gold

## Historical pool

- Discovered: 157412
- Ever alive: 29706
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
