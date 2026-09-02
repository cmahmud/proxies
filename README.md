# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 443
- HTTP: 105 alive / 79 gold
- HTTPS: 92 alive / 28 gold
- SOCKS4: 186 alive / 163 gold
- SOCKS5: 188 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47659
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
