# SyndProxy validated proxy pool

## Current pool

- Alive now: 460
- Gold now: 372
- HTTP: 83 alive / 56 gold
- HTTPS: 32 alive / 11 gold
- SOCKS4: 167 alive / 151 gold
- SOCKS5: 178 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48275
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
