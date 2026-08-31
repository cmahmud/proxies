# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 470
- HTTP: 146 alive / 99 gold
- HTTPS: 108 alive / 34 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 194 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45130
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
