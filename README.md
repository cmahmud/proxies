# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 374
- HTTP: 102 alive / 56 gold
- HTTPS: 48 alive / 12 gold
- SOCKS4: 169 alive / 151 gold
- SOCKS5: 187 alive / 155 gold

## Historical pool

- Discovered: 174129
- Ever alive: 33058
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
