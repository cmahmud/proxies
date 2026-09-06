# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 392
- HTTP: 109 alive / 70 gold
- HTTPS: 37 alive / 18 gold
- SOCKS4: 168 alive / 151 gold
- SOCKS5: 179 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48234
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
