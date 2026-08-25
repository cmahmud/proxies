# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 407
- HTTP: 102 alive / 65 gold
- HTTPS: 92 alive / 19 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 183 alive / 164 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35437
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
