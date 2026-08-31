# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 480
- HTTP: 144 alive / 99 gold
- HTTPS: 126 alive / 44 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 197 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45030
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
