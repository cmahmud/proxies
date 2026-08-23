# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 379
- HTTP: 96 alive / 64 gold
- HTTPS: 39 alive / 12 gold
- SOCKS4: 164 alive / 151 gold
- SOCKS5: 174 alive / 152 gold

## Historical pool

- Discovered: 174159
- Ever alive: 33077
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
