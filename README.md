# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 419
- HTTP: 140 alive / 74 gold
- HTTPS: 84 alive / 20 gold
- SOCKS4: 183 alive / 159 gold
- SOCKS5: 192 alive / 166 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33847
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
