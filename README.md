# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 425
- HTTP: 88 alive / 69 gold
- HTTPS: 97 alive / 31 gold
- SOCKS4: 171 alive / 156 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47295
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
