# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 473
- HTTP: 146 alive / 96 gold
- HTTPS: 115 alive / 39 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 203 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45105
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
