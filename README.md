# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 470
- HTTP: 147 alive / 96 gold
- HTTPS: 107 alive / 37 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 196 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45138
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
