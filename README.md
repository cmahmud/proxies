# SyndProxy validated proxy pool

## Current pool

- Alive now: 597
- Gold now: 427
- HTTP: 136 alive / 74 gold
- HTTPS: 92 alive / 25 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 194 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35179
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
