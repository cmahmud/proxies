# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 443
- HTTP: 103 alive / 79 gold
- HTTPS: 91 alive / 28 gold
- SOCKS4: 187 alive / 163 gold
- SOCKS5: 189 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47659
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
