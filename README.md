# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 403
- HTTP: 112 alive / 80 gold
- HTTPS: 67 alive / 17 gold
- SOCKS4: 166 alive / 151 gold
- SOCKS5: 183 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48081
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
