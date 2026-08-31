# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 477
- HTTP: 139 alive / 99 gold
- HTTPS: 125 alive / 43 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 193 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45034
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
