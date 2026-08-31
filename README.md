# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 456
- HTTP: 136 alive / 86 gold
- HTTPS: 106 alive / 34 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 214 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45350
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
