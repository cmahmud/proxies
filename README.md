# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 385
- HTTP: 106 alive / 55 gold
- HTTPS: 36 alive / 11 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 194 alive / 163 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33423
- Ever gold: 1237

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
