# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 443
- HTTP: 139 alive / 76 gold
- HTTPS: 105 alive / 34 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 208 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45373
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
