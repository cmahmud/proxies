# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 417
- HTTP: 116 alive / 69 gold
- HTTPS: 81 alive / 19 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35333
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
