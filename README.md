# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 461
- HTTP: 123 alive / 90 gold
- HTTPS: 125 alive / 38 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 190 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45667
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
