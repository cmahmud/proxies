# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 413
- HTTP: 87 alive / 58 gold
- HTTPS: 52 alive / 24 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47099
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
