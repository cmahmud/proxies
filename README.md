# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 427
- HTTP: 112 alive / 75 gold
- HTTPS: 69 alive / 26 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 196 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44342
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
