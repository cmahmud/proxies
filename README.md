# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 392
- HTTP: 125 alive / 59 gold
- HTTPS: 65 alive / 13 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 180 alive / 160 gold

## Historical pool

- Discovered: 179921
- Ever alive: 33508
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
