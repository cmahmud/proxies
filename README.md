# SyndProxy validated proxy pool

## Current pool

- Alive now: 445
- Gold now: 372
- HTTP: 72 alive / 50 gold
- HTTPS: 32 alive / 12 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 175 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48304
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
