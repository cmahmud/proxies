# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 454
- HTTP: 143 alive / 85 gold
- HTTPS: 102 alive / 32 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 219 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45362
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
