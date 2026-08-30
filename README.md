# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 422
- HTTP: 121 alive / 76 gold
- HTTPS: 66 alive / 23 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 198 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44337
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
