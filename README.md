# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 387
- HTTP: 96 alive / 54 gold
- HTTPS: 53 alive / 14 gold
- SOCKS4: 169 alive / 156 gold
- SOCKS5: 187 alive / 163 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33532
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
