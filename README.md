# SyndProxy private pool

## Current pool

- Alive now: 972
- Gold now: 393
- HTTP: 334 alive / 85 gold
- HTTPS: 180 alive / 20 gold
- SOCKS4: 203 alive / 129 gold
- SOCKS5: 255 alive / 159 gold

## Historical pool

- Discovered: 157412
- Ever alive: 29707
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
