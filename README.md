# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 407
- HTTP: 117 alive / 64 gold
- HTTPS: 55 alive / 15 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33676
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
