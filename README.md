# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 484
- HTTP: 142 alive / 100 gold
- HTTPS: 121 alive / 45 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 192 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45099
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
