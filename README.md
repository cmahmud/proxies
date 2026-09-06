# SyndProxy validated proxy pool

## Current pool

- Alive now: 443
- Gold now: 367
- HTTP: 72 alive / 56 gold
- HTTPS: 28 alive / 14 gold
- SOCKS4: 168 alive / 151 gold
- SOCKS5: 175 alive / 146 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48256
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
