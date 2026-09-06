# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 405
- HTTP: 105 alive / 77 gold
- HTTPS: 53 alive / 18 gold
- SOCKS4: 167 alive / 153 gold
- SOCKS5: 177 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48093
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
