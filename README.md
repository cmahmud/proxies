# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 427
- HTTP: 92 alive / 70 gold
- HTTPS: 74 alive / 24 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 180 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47681
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
