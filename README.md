# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 473
- HTTP: 147 alive / 96 gold
- HTTPS: 106 alive / 38 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 203 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45113
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
