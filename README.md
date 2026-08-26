# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 379
- HTTP: 118 alive / 68 gold
- HTTPS: 65 alive / 20 gold
- SOCKS4: 147 alive / 140 gold
- SOCKS5: 172 alive / 151 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38765
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
