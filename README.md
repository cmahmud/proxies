# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 413
- HTTP: 112 alive / 70 gold
- HTTPS: 60 alive / 18 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 189 alive / 166 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33709
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
