# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 390
- HTTP: 110 alive / 72 gold
- HTTPS: 34 alive / 13 gold
- SOCKS4: 167 alive / 151 gold
- SOCKS5: 185 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48215
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
