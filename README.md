# SyndProxy validated proxy pool

## Current pool

- Alive now: 667
- Gold now: 466
- HTTP: 163 alive / 97 gold
- HTTPS: 130 alive / 35 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 201 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45171
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
