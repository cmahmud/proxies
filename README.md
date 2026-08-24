# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 408
- HTTP: 111 alive / 65 gold
- HTTPS: 56 alive / 16 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 190 alive / 168 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33677
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
