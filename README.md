# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 375
- HTTP: 92 alive / 59 gold
- HTTPS: 49 alive / 12 gold
- SOCKS4: 164 alive / 150 gold
- SOCKS5: 180 alive / 154 gold

## Historical pool

- Discovered: 174134
- Ever alive: 33062
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
