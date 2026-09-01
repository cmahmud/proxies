# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 459
- HTTP: 144 alive / 92 gold
- HTTPS: 120 alive / 33 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 193 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46876
- Ever gold: 1453

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
