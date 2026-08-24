# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 414
- HTTP: 110 alive / 72 gold
- HTTPS: 59 alive / 18 gold
- SOCKS4: 181 alive / 159 gold
- SOCKS5: 192 alive / 165 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33708
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
