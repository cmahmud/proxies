# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 413
- HTTP: 109 alive / 71 gold
- HTTPS: 62 alive / 18 gold
- SOCKS4: 181 alive / 159 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33708
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
