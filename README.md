# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 394
- HTTP: 137 alive / 58 gold
- HTTPS: 83 alive / 14 gold
- SOCKS4: 177 alive / 157 gold
- SOCKS5: 185 alive / 165 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33525
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
