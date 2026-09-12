# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 427
- HTTP: 105 alive / 79 gold
- HTTPS: 46 alive / 27 gold
- SOCKS4: 167 alive / 156 gold
- SOCKS5: 177 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49449
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
