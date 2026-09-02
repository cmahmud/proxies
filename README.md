# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 439
- HTTP: 130 alive / 77 gold
- HTTPS: 113 alive / 24 gold
- SOCKS4: 192 alive / 164 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47620
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
