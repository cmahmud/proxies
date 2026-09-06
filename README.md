# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 404
- HTTP: 112 alive / 77 gold
- HTTPS: 61 alive / 19 gold
- SOCKS4: 176 alive / 151 gold
- SOCKS5: 184 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48072
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
