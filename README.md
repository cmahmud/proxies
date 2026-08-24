# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 408
- HTTP: 115 alive / 65 gold
- HTTPS: 55 alive / 15 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 187 alive / 169 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33677
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
