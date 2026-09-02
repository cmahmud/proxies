# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 430
- HTTP: 100 alive / 72 gold
- HTTPS: 90 alive / 22 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 189 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47672
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
