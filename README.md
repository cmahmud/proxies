# SyndProxy validated proxy pool

## Current pool

- Alive now: 600
- Gold now: 446
- HTTP: 126 alive / 79 gold
- HTTPS: 100 alive / 30 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 192 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47636
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
