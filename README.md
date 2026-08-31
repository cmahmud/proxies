# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 480
- HTTP: 140 alive / 101 gold
- HTTPS: 126 alive / 43 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 198 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45073
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
