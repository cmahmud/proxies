# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 413
- HTTP: 81 alive / 63 gold
- HTTPS: 113 alive / 26 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 181 alive / 166 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47223
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
