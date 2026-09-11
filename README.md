# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 400
- HTTP: 95 alive / 69 gold
- HTTPS: 39 alive / 21 gold
- SOCKS4: 162 alive / 137 gold
- SOCKS5: 193 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48770
- Ever gold: 1566

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
