# SyndProxy validated proxy pool

## Current pool

- Alive now: 613
- Gold now: 470
- HTTP: 134 alive / 96 gold
- HTTPS: 106 alive / 38 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 198 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45118
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
