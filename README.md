# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 405
- HTTP: 112 alive / 62 gold
- HTTPS: 50 alive / 15 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 181051
- Ever alive: 33674
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
