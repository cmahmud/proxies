# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 464
- HTTP: 132 alive / 93 gold
- HTTPS: 112 alive / 37 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 206 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44854
- Ever gold: 1416

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
