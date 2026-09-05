# SyndProxy validated proxy pool

## Current pool

- Alive now: 442
- Gold now: 314
- HTTP: 151 alive / 80 gold
- HTTPS: 31 alive / 17 gold
- SOCKS4: 83 alive / 73 gold
- SOCKS5: 177 alive / 144 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47820
- Ever gold: 1492

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
