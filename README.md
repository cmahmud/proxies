# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 417
- HTTP: 156 alive / 72 gold
- HTTPS: 93 alive / 18 gold
- SOCKS4: 183 alive / 159 gold
- SOCKS5: 193 alive / 168 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33843
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
