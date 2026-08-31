# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 441
- HTTP: 131 alive / 73 gold
- HTTPS: 109 alive / 32 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 218 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45374
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
