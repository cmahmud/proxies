# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 428
- HTTP: 102 alive / 73 gold
- HTTPS: 43 alive / 19 gold
- SOCKS4: 176 alive / 164 gold
- SOCKS5: 185 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48997
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
