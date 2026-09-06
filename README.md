# SyndProxy validated proxy pool

## Current pool

- Alive now: 418
- Gold now: 334
- HTTP: 79 alive / 55 gold
- HTTPS: 41 alive / 18 gold
- SOCKS4: 144 alive / 136 gold
- SOCKS5: 154 alive / 125 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48343
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
