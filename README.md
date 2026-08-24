# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 438
- HTTP: 136 alive / 80 gold
- HTTPS: 93 alive / 24 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 196 alive / 173 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34544
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
