# SyndProxy validated proxy pool

## Current pool

- Alive now: 426
- Gold now: 320
- HTTP: 84 alive / 58 gold
- HTTPS: 47 alive / 7 gold
- SOCKS4: 148 alive / 134 gold
- SOCKS5: 147 alive / 121 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48368
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
