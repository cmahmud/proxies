# SyndProxy validated proxy pool

## Current pool

- Alive now: 696
- Gold now: 459
- HTTP: 170 alive / 87 gold
- HTTPS: 112 alive / 36 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 236 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45328
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
