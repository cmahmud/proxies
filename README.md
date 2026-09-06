# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 402
- HTTP: 113 alive / 80 gold
- HTTPS: 65 alive / 17 gold
- SOCKS4: 168 alive / 151 gold
- SOCKS5: 183 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48078
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
