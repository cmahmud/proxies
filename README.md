# SyndProxy validated proxy pool

## Current pool

- Alive now: 613
- Gold now: 445
- HTTP: 125 alive / 79 gold
- HTTPS: 112 alive / 28 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 194 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47565
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
