# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 433
- HTTP: 130 alive / 79 gold
- HTTPS: 58 alive / 24 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34132
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
