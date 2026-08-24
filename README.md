# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 433
- HTTP: 133 alive / 80 gold
- HTTPS: 77 alive / 24 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34132
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
