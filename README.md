# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 424
- HTTP: 132 alive / 73 gold
- HTTPS: 90 alive / 21 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 198 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35152
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
