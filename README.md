# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 466
- HTTP: 143 alive / 96 gold
- HTTPS: 118 alive / 38 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45141
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
