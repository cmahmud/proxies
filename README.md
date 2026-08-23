# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 334
- HTTP: 104 alive / 40 gold
- HTTPS: 69 alive / 6 gold
- SOCKS4: 170 alive / 151 gold
- SOCKS5: 184 alive / 137 gold

## Historical pool

- Discovered: 171578
- Ever alive: 32894
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
