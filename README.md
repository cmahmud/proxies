# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 425
- HTTP: 97 alive / 72 gold
- HTTPS: 57 alive / 25 gold
- SOCKS4: 200 alive / 166 gold
- SOCKS5: 181 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49080
- Ever gold: 1572

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
