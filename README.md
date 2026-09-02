# SyndProxy validated proxy pool

## Current pool

- Alive now: 613
- Gold now: 448
- HTTP: 127 alive / 82 gold
- HTTPS: 112 alive / 30 gold
- SOCKS4: 185 alive / 164 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47638
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
