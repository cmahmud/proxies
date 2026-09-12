# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 419
- HTTP: 108 alive / 76 gold
- HTTPS: 46 alive / 19 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 176 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49458
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
