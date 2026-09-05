# SyndProxy validated proxy pool

## Current pool

- Alive now: 380
- Gold now: 292
- HTTP: 109 alive / 77 gold
- HTTPS: 40 alive / 19 gold
- SOCKS4: 76 alive / 65 gold
- SOCKS5: 155 alive / 131 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47884
- Ever gold: 1501

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
