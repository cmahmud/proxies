# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 347
- HTTP: 169 alive / 39 gold
- HTTPS: 50 alive / 9 gold
- SOCKS4: 183 alive / 154 gold
- SOCKS5: 240 alive / 145 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32873
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
