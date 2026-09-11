# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 404
- HTTP: 91 alive / 65 gold
- HTTPS: 34 alive / 20 gold
- SOCKS4: 159 alive / 147 gold
- SOCKS5: 186 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48800
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
