# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 449
- HTTP: 116 alive / 84 gold
- HTTPS: 52 alive / 30 gold
- SOCKS4: 167 alive / 162 gold
- SOCKS5: 184 alive / 173 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43680
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
