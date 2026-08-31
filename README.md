# SyndProxy validated proxy pool

## Current pool

- Alive now: 687
- Gold now: 456
- HTTP: 162 alive / 86 gold
- HTTPS: 115 alive / 35 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 231 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45330
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
