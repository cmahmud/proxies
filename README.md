# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 441
- HTTP: 100 alive / 76 gold
- HTTPS: 100 alive / 28 gold
- SOCKS4: 183 alive / 164 gold
- SOCKS5: 184 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47660
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
