# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 405
- HTTP: 135 alive / 80 gold
- HTTPS: 56 alive / 28 gold
- SOCKS4: 165 alive / 142 gold
- SOCKS5: 186 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48041
- Ever gold: 1515

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
