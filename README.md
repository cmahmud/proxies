# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 437
- HTTP: 122 alive / 80 gold
- HTTPS: 63 alive / 28 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43696
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
