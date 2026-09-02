# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 440
- HTTP: 104 alive / 79 gold
- HTTPS: 90 alive / 26 gold
- SOCKS4: 184 alive / 163 gold
- SOCKS5: 191 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47659
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
