# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 402
- HTTP: 98 alive / 64 gold
- HTTPS: 76 alive / 18 gold
- SOCKS4: 163 alive / 155 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34972
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
