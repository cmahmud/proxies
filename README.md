# SyndProxy validated proxy pool

## Current pool

- Alive now: 605
- Gold now: 473
- HTTP: 129 alive / 99 gold
- HTTPS: 104 alive / 38 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 199 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45119
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
