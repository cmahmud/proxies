# SyndProxy validated proxy pool

## Current pool

- Alive now: 664
- Gold now: 478
- HTTP: 152 alive / 106 gold
- HTTPS: 138 alive / 36 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 201 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45230
- Ever gold: 1427

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
