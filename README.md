# SyndProxy validated proxy pool

## Current pool

- Alive now: 447
- Gold now: 372
- HTTP: 73 alive / 51 gold
- HTTPS: 32 alive / 13 gold
- SOCKS4: 166 alive / 155 gold
- SOCKS5: 176 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48303
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
