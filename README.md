# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 451
- HTTP: 101 alive / 84 gold
- HTTPS: 53 alive / 32 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 190 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49195
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
