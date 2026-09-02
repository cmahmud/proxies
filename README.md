# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 437
- HTTP: 128 alive / 75 gold
- HTTPS: 121 alive / 25 gold
- SOCKS4: 185 alive / 163 gold
- SOCKS5: 196 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47612
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
