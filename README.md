# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 437
- HTTP: 104 alive / 77 gold
- HTTPS: 82 alive / 26 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 183 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47680
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
