# SyndProxy validated proxy pool

## Current pool

- Alive now: 394
- Gold now: 219
- HTTP: 147 alive / 58 gold
- HTTPS: 51 alive / 12 gold
- SOCKS4: 76 alive / 68 gold
- SOCKS5: 120 alive / 81 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32688
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
