# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 346
- HTTP: 106 alive / 38 gold
- HTTPS: 50 alive / 10 gold
- SOCKS4: 167 alive / 152 gold
- SOCKS5: 173 alive / 146 gold

## Historical pool

- Discovered: 171048
- Ever alive: 32856
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
