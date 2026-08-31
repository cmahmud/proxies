# SyndProxy validated proxy pool

## Current pool

- Alive now: 673
- Gold now: 468
- HTTP: 164 alive / 99 gold
- HTTPS: 132 alive / 34 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 201 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45172
- Ever gold: 1425

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
