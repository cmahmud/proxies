# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 485
- HTTP: 140 alive / 103 gold
- HTTPS: 114 alive / 46 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 198 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45069
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
