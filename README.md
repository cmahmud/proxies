# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 470
- HTTP: 146 alive / 95 gold
- HTTPS: 115 alive / 37 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 202 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45107
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
