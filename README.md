# SyndProxy validated proxy pool

## Current pool

- Alive now: 451
- Gold now: 365
- HTTP: 73 alive / 51 gold
- HTTPS: 30 alive / 11 gold
- SOCKS4: 172 alive / 153 gold
- SOCKS5: 176 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48301
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
