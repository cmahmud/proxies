# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 470
- HTTP: 144 alive / 98 gold
- HTTPS: 117 alive / 38 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 192 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45140
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
