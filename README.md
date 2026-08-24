# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 384
- HTTP: 105 alive / 54 gold
- HTTPS: 36 alive / 11 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 192 alive / 163 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33423
- Ever gold: 1237

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
