# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 450
- HTTP: 127 alive / 93 gold
- HTTPS: 64 alive / 35 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 199 alive / 164 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44254
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
