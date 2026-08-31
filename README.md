# SyndProxy validated proxy pool

## Current pool

- Alive now: 602
- Gold now: 436
- HTTP: 122 alive / 80 gold
- HTTPS: 97 alive / 26 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 207 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45460
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
