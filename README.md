# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 480
- HTTP: 145 alive / 99 gold
- HTTPS: 122 alive / 43 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 192 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45098
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
