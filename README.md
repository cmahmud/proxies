# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 404
- HTTP: 97 alive / 65 gold
- HTTPS: 32 alive / 20 gold
- SOCKS4: 167 alive / 146 gold
- SOCKS5: 193 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48787
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
