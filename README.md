# SyndProxy validated proxy pool

## Current pool

- Alive now: 604
- Gold now: 435
- HTTP: 118 alive / 79 gold
- HTTPS: 99 alive / 26 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 211 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45460
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
