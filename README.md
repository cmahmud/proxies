# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 470
- HTTP: 151 alive / 98 gold
- HTTPS: 106 alive / 35 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 194 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45132
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
