# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 431
- HTTP: 101 alive / 76 gold
- HTTPS: 53 alive / 24 gold
- SOCKS4: 185 alive / 164 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49132
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
