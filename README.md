# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 435
- HTTP: 100 alive / 75 gold
- HTTPS: 45 alive / 27 gold
- SOCKS4: 188 alive / 162 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49153
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
