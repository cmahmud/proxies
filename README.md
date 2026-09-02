# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 440
- HTTP: 97 alive / 79 gold
- HTTPS: 83 alive / 25 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 191 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47674
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
