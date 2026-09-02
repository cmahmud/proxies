# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 439
- HTTP: 136 alive / 74 gold
- HTTPS: 132 alive / 27 gold
- SOCKS4: 188 alive / 163 gold
- SOCKS5: 189 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47618
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
