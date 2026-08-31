# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 473
- HTTP: 155 alive / 102 gold
- HTTPS: 132 alive / 36 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 193 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45146
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
