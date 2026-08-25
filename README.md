# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 424
- HTTP: 103 alive / 67 gold
- HTTPS: 98 alive / 25 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 189 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35672
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
