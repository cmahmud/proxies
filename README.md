# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 433
- HTTP: 120 alive / 79 gold
- HTTPS: 107 alive / 23 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 186 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47656
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
