# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 400
- HTTP: 103 alive / 77 gold
- HTTPS: 53 alive / 17 gold
- SOCKS4: 168 alive / 151 gold
- SOCKS5: 175 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48093
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
