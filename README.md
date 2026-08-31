# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 480
- HTTP: 144 alive / 98 gold
- HTTPS: 130 alive / 47 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 202 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45014
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
