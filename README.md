# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 491
- HTTP: 155 alive / 105 gold
- HTTPS: 118 alive / 47 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 197 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44961
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
