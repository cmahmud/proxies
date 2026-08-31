# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 473
- HTTP: 134 alive / 96 gold
- HTTPS: 113 alive / 40 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 200 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45117
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
