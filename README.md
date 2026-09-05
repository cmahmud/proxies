# SyndProxy validated proxy pool

## Current pool

- Alive now: 389
- Gold now: 305
- HTTP: 104 alive / 76 gold
- HTTPS: 35 alive / 18 gold
- SOCKS4: 77 alive / 68 gold
- SOCKS5: 173 alive / 143 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47842
- Ever gold: 1498

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
