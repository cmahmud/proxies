# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 425
- HTTP: 92 alive / 70 gold
- HTTPS: 45 alive / 20 gold
- SOCKS4: 193 alive / 163 gold
- SOCKS5: 201 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48922
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
