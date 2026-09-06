# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 407
- HTTP: 130 alive / 82 gold
- HTTPS: 59 alive / 27 gold
- SOCKS4: 167 alive / 143 gold
- SOCKS5: 187 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48044
- Ever gold: 1515

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
