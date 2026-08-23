# SyndProxy validated proxy pool

## Current pool

- Alive now: 447
- Gold now: 374
- HTTP: 69 alive / 39 gold
- HTTPS: 31 alive / 13 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 174 alive / 162 gold

## Historical pool

- Discovered: 172867
- Ever alive: 32987
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
