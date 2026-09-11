# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 451
- HTTP: 109 alive / 86 gold
- HTTPS: 47 alive / 29 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 185 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49188
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
