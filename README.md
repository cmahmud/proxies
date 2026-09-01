# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 420
- HTTP: 87 alive / 68 gold
- HTTPS: 85 alive / 26 gold
- SOCKS4: 170 alive / 157 gold
- SOCKS5: 175 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47254
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
