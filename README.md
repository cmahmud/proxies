# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 412
- HTTP: 110 alive / 70 gold
- HTTPS: 61 alive / 18 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33709
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
