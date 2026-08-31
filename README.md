# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 440
- HTTP: 122 alive / 80 gold
- HTTPS: 92 alive / 25 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 201 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45457
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
