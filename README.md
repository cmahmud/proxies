# SyndProxy validated proxy pool

## Current pool

- Alive now: 426
- Gold now: 332
- HTTP: 84 alive / 60 gold
- HTTPS: 41 alive / 13 gold
- SOCKS4: 153 alive / 136 gold
- SOCKS5: 148 alive / 123 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48354
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
