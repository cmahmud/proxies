# SyndProxy validated proxy pool

## Current pool

- Alive now: 613
- Gold now: 440
- HTTP: 123 alive / 76 gold
- HTTPS: 112 alive / 28 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 198 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47566
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
