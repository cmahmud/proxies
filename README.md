# SyndProxy validated proxy pool

## Current pool

- Alive now: 716
- Gold now: 460
- HTTP: 170 alive / 86 gold
- HTTPS: 131 alive / 37 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 236 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45332
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
