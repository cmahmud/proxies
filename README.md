# SyndProxy validated proxy pool

## Current pool

- Alive now: 427
- Gold now: 336
- HTTP: 85 alive / 59 gold
- HTTPS: 43 alive / 17 gold
- SOCKS4: 151 alive / 133 gold
- SOCKS5: 148 alive / 127 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48345
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
