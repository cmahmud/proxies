# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 442
- HTTP: 137 alive / 76 gold
- HTTPS: 116 alive / 30 gold
- SOCKS4: 188 alive / 165 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47641
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
