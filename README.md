# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 413
- HTTP: 109 alive / 70 gold
- HTTPS: 63 alive / 18 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 190 alive / 166 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33709
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
