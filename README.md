# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 446
- HTTP: 142 alive / 78 gold
- HTTPS: 116 alive / 29 gold
- SOCKS4: 181 alive / 165 gold
- SOCKS5: 187 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47622
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
