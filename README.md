# SyndProxy validated proxy pool

## Current pool

- Alive now: 382
- Gold now: 209
- HTTP: 117 alive / 50 gold
- HTTPS: 75 alive / 8 gold
- SOCKS4: 75 alive / 67 gold
- SOCKS5: 115 alive / 84 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32698
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
