# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 426
- HTTP: 103 alive / 79 gold
- HTTPS: 46 alive / 25 gold
- SOCKS4: 165 alive / 156 gold
- SOCKS5: 177 alive / 166 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49449
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
