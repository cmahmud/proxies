# SyndProxy validated proxy pool

## Current pool

- Alive now: 597
- Gold now: 423
- HTTP: 136 alive / 72 gold
- HTTPS: 94 alive / 21 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 197 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35149
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
