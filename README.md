# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 428
- HTTP: 114 alive / 74 gold
- HTTPS: 42 alive / 19 gold
- SOCKS4: 179 alive / 164 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48981
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
