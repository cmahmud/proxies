# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 425
- HTTP: 144 alive / 75 gold
- HTTPS: 93 alive / 24 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 195 alive / 167 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35187
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
