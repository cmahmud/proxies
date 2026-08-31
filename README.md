# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 426
- HTTP: 106 alive / 66 gold
- HTTPS: 61 alive / 26 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 202 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45539
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
