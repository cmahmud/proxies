# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 387
- HTTP: 140 alive / 71 gold
- HTTPS: 163 alive / 20 gold
- SOCKS4: 161 alive / 146 gold
- SOCKS5: 180 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39814
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
