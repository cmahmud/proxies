# SyndProxy validated proxy pool

## Current pool

- Alive now: 720
- Gold now: 458
- HTTP: 168 alive / 86 gold
- HTTPS: 135 alive / 35 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 239 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45333
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
