# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 441
- HTTP: 138 alive / 82 gold
- HTTPS: 74 alive / 26 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 190 alive / 173 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34730
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
