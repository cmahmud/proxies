# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 455
- HTTP: 120 alive / 83 gold
- HTTPS: 112 alive / 36 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 190 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45627
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
