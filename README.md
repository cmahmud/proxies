# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 362
- HTTP: 145 alive / 78 gold
- HTTPS: 61 alive / 23 gold
- SOCKS4: 141 alive / 115 gold
- SOCKS5: 173 alive / 146 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47989
- Ever gold: 1507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
