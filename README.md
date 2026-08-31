# SyndProxy validated proxy pool

## Current pool

- Alive now: 653
- Gold now: 485
- HTTP: 158 alive / 106 gold
- HTTPS: 123 alive / 40 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 199 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45243
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
