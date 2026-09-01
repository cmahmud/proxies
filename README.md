# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 413
- HTTP: 86 alive / 65 gold
- HTTPS: 80 alive / 22 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47194
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
