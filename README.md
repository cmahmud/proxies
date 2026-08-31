# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 462
- HTTP: 152 alive / 95 gold
- HTTPS: 117 alive / 36 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45144
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
