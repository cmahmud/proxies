# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 441
- HTTP: 110 alive / 82 gold
- HTTPS: 54 alive / 27 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49172
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
