# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 400
- HTTP: 106 alive / 76 gold
- HTTPS: 57 alive / 19 gold
- SOCKS4: 170 alive / 150 gold
- SOCKS5: 175 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48093
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
