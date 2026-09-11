# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 421
- HTTP: 90 alive / 67 gold
- HTTPS: 48 alive / 23 gold
- SOCKS4: 193 alive / 167 gold
- SOCKS5: 183 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49068
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
