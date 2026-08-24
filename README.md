# SyndProxy validated proxy pool

## Current pool

- Alive now: 587
- Gold now: 393
- HTTP: 137 alive / 58 gold
- HTTPS: 87 alive / 13 gold
- SOCKS4: 176 alive / 157 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33525
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
