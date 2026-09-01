# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 418
- HTTP: 90 alive / 67 gold
- HTTPS: 92 alive / 25 gold
- SOCKS4: 170 alive / 157 gold
- SOCKS5: 176 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47254
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
