# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 443
- HTTP: 144 alive / 76 gold
- HTTPS: 118 alive / 28 gold
- SOCKS4: 184 alive / 165 gold
- SOCKS5: 186 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47620
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
